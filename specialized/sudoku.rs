#!./make.py --10
// from @raffimolero / redstoneboi https://www.reddit.com/r/rust/comments/183ex3i/comment/kaoxj74/?context=3

//INFO: algo with specialized types

use std::{
    fmt::{Display, Formatter},
    fs,
    iter::FromIterator,
    ops::{Add, AddAssign, Sub, SubAssign},
    str::FromStr,
};

#[derive(Clone, Eq, PartialEq)]
struct Grid {
    data: [NumSet; 81],
    spaces: SpaceSet,
}

#[derive(Copy, Clone, Eq, PartialEq)]
struct NumSet(u16);

impl NumSet {
    const ALL: Self = Self(0b_111_111_111);
    const EMPTY: Self = Self(0);

    fn one_hot(val: u8) -> Self {
        Self(1 << val)
    }

    fn val(self) -> u8 {
        self.0.trailing_zeros() as u8
    }

    fn len(self) -> u32 {
        self.0.count_ones()
    }
}

impl FromIterator<Self> for NumSet {
    fn from_iter<T: IntoIterator<Item = Self>>(iter: T) -> Self {
        iter.into_iter()
            .reduce(|a, b| a + b)
            .expect("iterator must have more than 1 value")
    }
}

impl Add for NumSet {
    type Output = Self;
    fn add(self, rhs: Self) -> Self {
        NumSet(self.0 | rhs.0)
    }
}

impl AddAssign for NumSet {
    fn add_assign(&mut self, rhs: Self) {
        *self = *self + rhs;
    }
}

impl Sub for NumSet {
    type Output = Self;
    fn sub(self, rhs: Self) -> Self {
        NumSet(self.0 & !rhs.0)
    }
}

impl SubAssign for NumSet {
    fn sub_assign(&mut self, rhs: Self) {
        *self = *self - rhs;
    }
}

struct NumSetIter {
    set: NumSet,
    mask: u16,
}

impl Iterator for NumSetIter {
    type Item = NumSet;

    fn next(&mut self) -> Option<Self::Item> {
        loop {
            self.mask >>= 1;
            if self.mask == 0 {
                return None;
            }
            let masked = self.set.0 & self.mask;
            if masked != 0 {
                return Some(NumSet(masked));
            }
        }
    }
}

impl IntoIterator for NumSet {
    type Item = NumSet;
    type IntoIter = NumSetIter;
    fn into_iter(self) -> NumSetIter {
        NumSetIter {
            set: self,
            mask: 1 << 9,
        }
    }
}

#[derive(Clone, Eq, PartialEq)]
struct SpaceSet {
    data: [usize; 81],
    len: usize,
}

impl FromIterator<usize> for SpaceSet {
    fn from_iter<T: IntoIterator<Item = usize>>(iter: T) -> Self {
        let mut out = Self::empty();
        for n in iter {
            out.insert(n);
        }
        out
    }
}

impl SpaceSet {
    fn empty() -> Self {
        Self {
            data: [0; 81],
            len: 0,
        }
    }

    fn insert(&mut self, item: usize) {
        self.data[self.len] = item;
        self.len += 1;
    }

    fn remove(&mut self, index: usize) {
        self.len -= 1;
        self.data[index] = self.data[self.len];
    }

    fn iter(&self) -> impl '_ + Iterator<Item = usize> {
        self.data[..self.len].iter().copied()
    }

    /// creates a new SpaceSet to track all the holes in the grid
    fn find_all(data: &[NumSet; 81]) -> Self {
        data.iter()
            .enumerate()
            .filter_map(|(i, n)| (*n == NumSet::EMPTY).then_some(i))
            .collect()
    }
}

impl Grid {
    fn sqr(&self, x: usize, y: usize) -> NumSet {
        let x = (x / 3) * 3;
        let y = (y / 3) * 3;
        let i = y * 9 + x;
        NumSet::from_iter(
            self.data[i..i + 3]
                .iter()
                .chain(&self.data[i + 9..i + 12])
                .chain(&self.data[i + 18..i + 21])
                .copied(),
        )
    }

    fn col(&self, x: usize) -> NumSet {
        NumSet::from_iter((0..9).map(|y| self.data[y * 9 + x]))
    }

    fn row(&self, y: usize) -> NumSet {
        NumSet::from_iter(self.data[y * 9..(y + 1) * 9].iter().copied())
    }

    fn free(&self, x: usize, y: usize) -> NumSet {
        let col = self.col(x);
        let row = self.row(y);
        let sqr = self.sqr(x, y);
        NumSet::ALL - (col + row + sqr)
    }

    fn resolv(&mut self) -> bool {
        let mut best_space_index = 0;
        let mut best_space = 0;
        let mut best_set = NumSet::ALL;
        let mut best_set_len = 10;
        for (i, space) in self.spaces.iter().enumerate() {
            let free = self.free(space % 9, space / 9);
            let set_len = free.len();
            if set_len == 0 {
                // Unsolvable.
                return false;
            }
            if set_len < best_set_len {
                // Found better candidate set, update all.
                best_space_index = i;
                best_space = space;
                best_set = free;
                best_set_len = set_len;
            }
            if set_len == 1 {
                // Only one candidate here; we can't do better.
                break;
            }
        }

        if best_set_len == 10 {
            // Best set was never updated. Solved.
            return true;
        };

        self.spaces.remove(best_space_index);
        for c in best_set {
            self.data[best_space] = c;
            if self.resolv() {
                return true;
            }
        }
        self.data[best_space] = NumSet::EMPTY;
        self.spaces.insert(best_space);

        false
    }
}

#[derive(Debug, PartialEq, Eq)]
struct ParseGridError {
    pos: usize,
}

impl FromStr for Grid {
    type Err = ParseGridError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut data = [NumSet::EMPTY; 81];
        for (i, (g, c)) in data.iter_mut().zip(s.chars()).enumerate() {
            match c {
                '1'..='9' => *g = NumSet::one_hot(c as u8 - b'1'),
                '.' => {}
                _ => return Err(ParseGridError { pos: i }),
            }
        }
        let spaces = SpaceSet::find_all(&data);
        Ok(Grid { data, spaces })
    }
}

impl Display for Grid {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result<(), std::fmt::Error> {
        for g in self.data {
            let c = match g {
                NumSet::EMPTY => '.',
                _ => (b'1' + g.val()) as char,
            };
            write!(f, "{c}")?;
        }
        Ok(())
    }
}

// fn main() -> Result<(), Box<dyn std::error::Error>> {
//     let content = fs::read_to_string("grids.txt")?;
//     let gg: Vec<&str> = content.lines().take(1956).collect();

//     for line in gg {
//         let mut grid: Grid = line.trim().parse().unwrap();
//         grid.resolv();
//         println!("{} ", grid);
//     }
//     Ok(())
// }

fn main() {
    // Iterate over the lines in io::stdin()
    for line in io::stdin().lines() {
        let mut grid: Grid = line.unwrap().trim().parse().unwrap();
        grid.resolv();
        println!("{} ", grid);
    }
}
