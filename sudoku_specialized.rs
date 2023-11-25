#!./make.py
//INFO: the simple algo, with specialized types (100grids)

// from @raffimolero / redstoneboi https://www.reddit.com/r/rust/comments/183ex3i/comment/kaoxj74/?context=3

use std::{fmt::Display, fs, ops::SubAssign, str::FromStr};
use std::convert::TryFrom;

struct NumSet([bool; 9]);

impl NumSet {
    fn all() -> Self {
        Self([true; 9])
    }

    fn iter<'a>(&'a self) -> impl 'a + Iterator<Item = u8> {
        self.0
            .iter()
            .enumerate()
            .filter_map(|(i, v)| v.then(|| i as u8))
    }
}

impl<T: IntoIterator<Item = u8>> SubAssign<T> for NumSet {
    fn sub_assign(&mut self, rhs: T) {
        for n in rhs {
            if n == EMPTY {
                continue;
            }
            self.0[n as usize] = false;
        }
    }
}

struct Grid {
    data: [u8; 81],
}

impl FromStr for Grid {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut data = <[u8; 81]>::try_from(s.as_bytes()).map_err(|_| ())?;
        for c in data.iter_mut() {
            *c = match c {
                b'.' => EMPTY,
                _ => *c - ZERO_IDX,
            };
        }
        Ok(Self { data })
    }
}

impl Display for Grid {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        for &n in &self.data {
            let c = match n {
                EMPTY => b'.',
                _ => n + ZERO_IDX,
            } as char;
            write!(f, "{c}")?;
        }
        Ok(())
    }
}

const EMPTY: u8 = 255;
const ZERO_IDX: u8 = b'1';

impl Grid {
    fn sqr<'a>(&'a self, x: usize, y: usize) -> impl 'a + Iterator<Item = u8> {
        let x = (x / 3) * 3;
        let y = (y / 3) * 3;
        let i = y * 9 + x;
        self.data[i..i + 3]
            .iter()
            .chain(&self.data[i + 9..i + 9 + 3])
            .chain(&self.data[i + 18..i + 18 + 3])
            .copied()
    }

    fn col<'a>(&'a self, x: usize) -> impl 'a + Iterator<Item = u8> {
        (0..9).map(move |y| self.data[x + y * 9])
    }

    fn row<'a>(&'a self, y: usize) -> impl 'a + Iterator<Item = u8> {
        self.data[y * 9..y * 9 + 9].iter().copied()
    }

    fn free(&self, x: usize, y: usize) -> NumSet {
        let mut all_chars: NumSet = NumSet::all();
        all_chars -= self.row(y);
        all_chars -= self.col(x);
        all_chars -= self.sqr(x, y);
        all_chars
    }

    fn resolv_inner(&mut self, pos: usize) -> bool {
        let Some(mut i) = self.data[pos..].iter().position(|c| *c == EMPTY) else {
            return true;
        };
        i += pos;
        for elem in self.free(i % 9, i / 9).iter() {
            self.data[i] = elem;
            if self.resolv_inner(i) {
                return true;
            }
            self.data[i] = EMPTY;
        }
        false
    }
}

fn resolv(g: &str) -> Option<String> {
    let mut g = g.parse::<Grid>().unwrap();
    g.resolv_inner(0).then(|| g.to_string())
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let content = fs::read_to_string("grids.txt")?;
    let gg: Vec<&str> = content.lines().take(100).collect();

    let t = std::time::Instant::now();
    for g in gg {
        if let Some(rg) = resolv(g) {
            if rg.chars().any(|c| c == '.') {
                panic!("not resolved ?!");
            }
            println!("{}", rg);
        }
    }
    println!("Took: {} s", (t.elapsed().as_millis() as f32) / 1000.0);
    Ok(())
}
