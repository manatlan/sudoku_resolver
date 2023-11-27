#!./make.py
// from @raffimolero / redstoneboi https://www.reddit.com/r/rust/comments/183ex3i/comment/kaoxj74/?context=3

//INFO: the optimized algo, with specialized types (and readable) (1956grids)

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
    const NIL: Self = Self(0b_111_111_111_1);
    const EMPTY: Self = Self(0);

    fn one_hot(val: u8) -> Self {
        NumSet(1 << val)
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
        while self.mask < (1 << 9) {
            let masked = self.set.0 & self.mask;
            self.mask <<= 1;
            if masked != 0 {
                return Some(NumSet(masked));
            }
        }
        None
    }
}

impl IntoIterator for NumSet {
    type Item = NumSet;
    type IntoIter = NumSetIter;
    fn into_iter(self) -> NumSetIter {
        NumSetIter { set: self, mask: 1 }
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
                .chain(self.data[i + 9..i + 12].iter())
                .chain(self.data[i + 18..i + 21].iter())
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
        let mut ibest = 0;
        let mut sbest = 0;
        let mut cbest = NumSet::NIL;
        for (i, s) in self.spaces.iter().enumerate() {
            let c = self.free(s % 9, s / 9);
            if c.len() == 0 {
                // unsolvable
                return false;
            }
            if c.len() < cbest.len() {
                ibest = i;
                sbest = s;
                cbest = c;
            }
            if c.len() == 1 {
                // Only one candidate here; we can't do better...
                break;
            }
        }

        if cbest == NumSet::NIL {
            // solved
            return true;
        };

        self.spaces.remove(ibest);
        for c in cbest {
            self.data[sbest] = c;
            if self.resolv() {
                return true;
            }
        }
        self.data[sbest] = NumSet::EMPTY;
        self.spaces.insert(sbest);

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

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let content = fs::read_to_string("grids.txt")?;
    let gg: Vec<&str> = content.lines().take(1956).collect();

    let t = std::time::Instant::now();
    for line in gg {
        let mut grid: Grid = line.trim().parse().unwrap();
        grid.resolv();
        println!("{} ", grid);
    }
    println!("Took: {} s", (t.elapsed().as_millis() as f32) / 1000.0);
    Ok(())
}
