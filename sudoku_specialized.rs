#!./make.py
//INFO: the simple algo, with specialized types (100grids)

// from @raffimolero / redstoneboi https://www.reddit.com/r/rust/comments/183ex3i/comment/kaoxj74/?context=3
use std::convert::TryFrom;
use std::{fmt::Display, fs, str::FromStr};

struct NumSet(u16);

impl NumSet {
    fn all() -> Self {
        Self(0b0000_0011_1111_1111)
    }

    fn iter(&self) -> impl '_ + Iterator<Item = u8> {
        (1..10u8).filter(move |&b| (1u16 << b) & self.0 > 0)
    }

    fn difference(&self, other: &Self) -> Self {
        NumSet(self.0 & !other.0)
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
            *c = c.saturating_sub(ZERO_IDX)
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

const EMPTY: u8 = 0;
const ZERO_IDX: u8 = b'0';

impl Grid {
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

    fn col(&self, x: usize) -> impl '_ + Iterator<Item = u8> {
        (0..9).map(move |y| self.data[x + y * 9])
    }

    fn row(&self, y: usize) -> impl '_ + Iterator<Item = u8> {
        self.data[y * 9..y * 9 + 9].iter().copied()
    }

    fn free(&self, x: usize, y: usize) -> NumSet {
        let numbers_found = NumSet(
            self.row(y)
                .chain(self.col(x))
                .chain(self.sqr(x, y))
                .fold(0u16, |acc, b| acc | 1u16 << (b - b'0')),
        );

        NumSet::all().difference(&numbers_found)
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

    for g in gg {
        if let Some(rg) = resolv(g) {
            println!("{}", rg);
        }
    }
    Ok(())
}
