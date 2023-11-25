#!./make.py
// from @raffimolero / redstoneboi https://www.reddit.com/r/rust/comments/183ex3i/comment/kaoxj74/?context=3

//INFO: the optimized algo, with specialized types (and readable) (1956grids)

use std::{fmt::Display, fs, ops::SubAssign, str::FromStr};
use std::iter::FromIterator;
use std::convert::TryFrom;

/// A Set intended to contain every valid number an empty tile could be
struct NumSet([bool; 9]);

impl NumSet {
    /// creates a new set where any number is possible
    fn all() -> Self {
        Self([true; 9])
    }

    fn iter(&self) -> impl '_ + Iterator<Item = u8> {
        self.0
            .iter()
            .enumerate()
            .filter_map(|(i, v)| v.then(|| i as u8))
    }

    /// returns how many possibilities there are for this tile
    fn len(&self) -> u8 {
        self.0.iter().filter(|n| **n).count() as u8
    }
}

impl<T: IntoIterator<Item = u8>> SubAssign<T> for NumSet {
    fn sub_assign(&mut self, rhs: T) {
        for n in rhs {
            if n == Grid::EMPTY {
                continue;
            }
            self.0[n as usize] = false;
        }
    }
}

/// A Set intended to contain every hole inside the sudoku board.
struct SpaceSet {
    data: [u8; 81],
    len: usize,
}

impl FromIterator<u8> for SpaceSet {
    fn from_iter<T: IntoIterator<Item = u8>>(iter: T) -> Self {
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

    fn insert(&mut self, item: u8) {
        self.data[self.len] = item;
        self.len += 1;
    }

    fn remove(&mut self, index: usize) {
        self.len -= 1;
        self.data[index] = self.data[self.len];
    }

    fn iter(&self) -> impl '_ + Iterator<Item = u8> {
        self.data[..self.len].iter().copied()
    }

    /// creates a new SpaceSet to track all the holes in the grid
    fn find_all(grid: &Grid) -> Self {
        grid.data
            .iter()
            .enumerate()
            .filter_map(|(i, n)| (*n == Grid::EMPTY).then_some(i as u8))
            .collect()
    }

    // NOTE: this is quite heavily coupled to the implementation details of Grid.
    // i could make it as generic as Iterator::min_by_key, but it is not necessary.
    /// finds a tile in the grid with the fewest possible outcomes
    fn pop_min(&mut self, grid: &Grid) -> Option<(u8, NumSet)> {
        let (i, out) = self
            .iter()
            .map(|space| (space, grid.free(space as usize % 9, space as usize / 9)))
            .enumerate()
            .min_by_key(|(_i, (_space, num_set))| num_set.len())?;
        self.remove(i);
        Some(out)
    }
}

/// a sudoku grid where empty tiles are 255 and numbers range from 0..=8
struct Grid {
    data: [u8; 81],
}

impl FromStr for Grid {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut data = <[u8; 81]>::try_from(s.as_bytes()).map_err(|_| ())?;
        for c in data.iter_mut() {
            *c = match c {
                b'.' => Grid::EMPTY,
                _ => *c - Grid::ZERO_IDX,
            };
        }
        Ok(Self { data })
    }
}

impl Display for Grid {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        for &n in &self.data {
            let c = match n {
                Grid::EMPTY => b'.',
                _ => n + Grid::ZERO_IDX,
            } as char;
            write!(f, "{c}")?;
        }
        Ok(())
    }
}

impl Grid {
    const EMPTY: u8 = 255;
    const ZERO_IDX: u8 = b'1';

    /// returns the values of all tiles in the block that a tile belongs to
    fn sqr(&self, x: usize, y: usize) -> impl '_ + Iterator<Item = u8> {
        let x = (x / 3) * 3;
        let y = (y / 3) * 3;
        let i = y * 9 + x;
        self.data[i..i + 3]
            .iter()
            .chain(&self.data[i + 9..i + 9 + 3])
            .chain(&self.data[i + 18..i + 18 + 3])
            .copied()
    }

    /// returns the values of all tiles in the column that a tile belongs to
    fn col(&self, x: usize) -> impl '_ + Iterator<Item = u8> {
        (0..9).map(move |y| self.data[x + y * 9])
    }

    /// returns the values of all tiles in the row that a tile belongs to
    fn row(&self, y: usize) -> impl '_ + Iterator<Item = u8> {
        self.data[y * 9..y * 9 + 9].iter().copied()
    }

    /// finds all the possible values that a given tile can be
    fn free(&self, x: usize, y: usize) -> NumSet {
        let mut all_chars: NumSet = NumSet::all();
        all_chars -= self.row(y);
        all_chars -= self.col(x);
        all_chars -= self.sqr(x, y);
        all_chars
    }

    fn resolve_inner(&mut self, spaces: &mut SpaceSet) -> bool {
        let Some((i, set)) = spaces.pop_min(self) else {
            return true;
        };
        for elem in set.iter() {
            self.data[i as usize] = elem;
            if self.resolve_inner(spaces) {
                return true;
            }
            self.data[i as usize] = Grid::EMPTY;
        }
        spaces.insert(i);
        false
    }

    /// attempts to solve the board through mutation, and returns true if it is solved
    /// returns false if it is unsolvable, and i believe it returns to its original state as well
    fn resolve(&mut self) -> bool {
        let mut spaces = SpaceSet::find_all(self);
        self.resolve_inner(&mut spaces)
    }
}

fn resolve_str(g: &str) -> Option<String> {
    let mut g = g.parse::<Grid>().unwrap();
    g.resolve().then(|| g.to_string())
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let content = fs::read_to_string("grids.txt")?;
    let gg: Vec<&str> = content.lines().take(1956).collect();

    let t = std::time::Instant::now();
    for g in gg {
        if let Some(rg) = resolve_str(g) {
            if rg.chars().any(|c| c == '.') {
                panic!("not resolved ?!");
            }
            println!("{}", rg);
        }
    }
    println!("Took: {} s", (t.elapsed().as_millis() as f32) / 1000.0);
    Ok(())
}
