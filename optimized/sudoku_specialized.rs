#!./make.py
// optimized version by 2e71828 see https://users.rust-lang.org/u/2e71828

//INFO: the optimized algo, with ultra-specialized types/api (1956grids)

use std::{
    fmt::{Display, Formatter},
    fs,
    ops::{Add, AddAssign, Sub, SubAssign},
    str::FromStr,
};

#[derive(Clone, Eq, PartialEq)]
struct Grid([CandidateSet; 81]);

#[derive(Copy, Clone, Eq, PartialEq)]
struct CandidateSet(u16);

impl CandidateSet {
    const ALL: Self = Self(0b_111_111_111);
    const EMPTY: Self = Self(0);

    fn one_hot(val: u8) -> Self {
        CandidateSet(1 << val)
    }

    fn val(self) -> u8 {
        self.0.trailing_zeros() as u8
    }

    fn from_iter(it: impl IntoIterator<Item = Self>) -> Self {
        it.into_iter()
            .reduce(|a, b| a + b)
            .expect("iterator must have more than 1 value")
    }

    fn len(self) -> u32 {
        self.0.count_ones()
    }
}

impl Add for CandidateSet {
    type Output = Self;
    fn add(self, rhs: Self) -> Self {
        CandidateSet(self.0 | rhs.0)
    }
}

impl AddAssign for CandidateSet {
    fn add_assign(&mut self, rhs: Self) {
        *self = *self + rhs;
    }
}

impl Sub for CandidateSet {
    type Output = Self;
    fn sub(self, rhs: Self) -> Self {
        CandidateSet(self.0 & !rhs.0)
    }
}

impl SubAssign for CandidateSet {
    fn sub_assign(&mut self, rhs: Self) {
        *self = *self - rhs;
    }
}

struct CandidateIter {
    set: CandidateSet,
    mask: u16,
}

impl Iterator for CandidateIter {
    type Item = CandidateSet;

    fn next(&mut self) -> Option<Self::Item> {
        while self.mask <= (1 << 9) {
            let masked = self.set.0 & self.mask;
            self.mask <<= 1;
            if masked != 0 {
                return Some(CandidateSet(masked));
            }
        }
        None
    }
}

impl IntoIterator for CandidateSet {
    type Item = CandidateSet;
    type IntoIter = CandidateIter;
    fn into_iter(self) -> CandidateIter {
        CandidateIter { set: self, mask: 1 }
    }
}

impl Grid {
    fn sqr(&self, x: usize, y: usize) -> CandidateSet {
        let x = (x / 3) * 3;
        let y = (y / 3) * 3;
        let i = y * 9 + x;
        CandidateSet::from_iter(self.0[i..i + 3].iter().copied())
            + CandidateSet::from_iter(self.0[i + 9..i + 12].iter().copied())
            + CandidateSet::from_iter(self.0[i + 18..i + 21].iter().copied())
    }

    fn col(&self, x: usize) -> CandidateSet {
        CandidateSet::from_iter((0..9).map(|y| self.0[y * 9 + x]))
    }

    fn row(&self, y: usize) -> CandidateSet {
        CandidateSet::from_iter(self.0[y * 9..(y + 1) * 9].iter().copied())
    }

    fn free(&self, x: usize, y: usize) -> CandidateSet {
        let col = self.col(x);
        let row = self.row(y);
        let sqr = self.sqr(x, y);
        CandidateSet::ALL - (col + row + sqr)
    }

    fn resolv(&mut self) -> bool {
        let mut ibest = None;
        let mut cbest = CandidateSet::ALL;
        for i in 0..81 {
            if self.0[i] == CandidateSet::EMPTY {
                let c = self.free(i % 9, i / 9);
                if c.len() == 0 {
                    // unsolvable
                    return false;
                }
                if c.len() < cbest.len() {
                    ibest = Some(i);
                    cbest = c;
                }
                if c.len() == 1 {
                    // Only one candidate here; we can't do better...
                    break;
                }
            }
        }

        let i = match ibest {
            None => return true, // solved
            Some(i) => i,
        };

        for c in cbest {
            self.0[i] = c;
            if self.resolv() {
                return true;
            }
        }
        self.0[i] = CandidateSet::EMPTY;
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
        let mut grid = [CandidateSet::EMPTY; 81];
        for (i, (g, c)) in grid.iter_mut().zip(s.chars()).enumerate() {
            if ('1'..='9').contains(&c) {
                *g = CandidateSet::one_hot(c as u8 - b'1');
            } else if c != '.' {
                return Err(ParseGridError { pos: i });
            }
        }
        Ok(Grid(grid))
    }
}

impl Display for Grid {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result<(), std::fmt::Error> {
        for g in self.0 {
            write!(
                f,
                "{}",
                match g {
                    CandidateSet::EMPTY => '.',
                    _ => (b'1' + g.val()) as char,
                }
            )?;
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
