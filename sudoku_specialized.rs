#!/usr/bin/rustc -C opt-level=3 -C target-cpu=native sudoku_specialized.rs -o sudoku && ./sudoku
//INFO: the simple algo, with specialized rust-types

// optimized version by 2e71828 see https://users.rust-lang.org/u/2e71828
// see https://users.rust-lang.org/t/is-rust-slow-too-fast/101796/8?u=manatlan
use std::fs;
use std::fmt::Formatter;
use std::str::FromStr;
use std::fmt::Display;
use std::ops::AddAssign;
use std::ops::SubAssign;
use std::ops::Sub;
use std::ops::Add;

#[derive(Clone,Eq,PartialEq)]
struct Grid([Option<u8>;81]);

#[derive(Copy,Clone,Eq,PartialEq)]
struct CandidateSet(u16);

impl CandidateSet {
    fn all()->Self { CandidateSet(0x1ff) }
    fn empty()->Self { CandidateSet(0) }
    fn singleton(val:u8)->Self { CandidateSet(1 << val) }
    fn from_iter(it: impl Iterator<Item=u8>)->Self {
        let mut ret = Self::empty();
        for i in it {
            ret += Self::singleton(i);
        }
        ret
    }
}

impl Add for CandidateSet {
    type Output = Self;
    fn add(self, rhs: Self)->Self { CandidateSet(self.0 | rhs.0) }
}

impl AddAssign for CandidateSet {
    fn add_assign(&mut self, rhs: Self) { *self = *self + rhs; }
}

impl Sub for CandidateSet {
    type Output = Self;
    fn sub(self, rhs: Self)->Self { CandidateSet(self.0 & !rhs.0) }
}

impl SubAssign for CandidateSet {
    fn sub_assign(&mut self, rhs: Self) { *self = *self - rhs; }
}

struct CandidateIter {
    set: CandidateSet,
    pos: u8
}

impl Iterator for CandidateIter {
    type Item = u8;
    fn next(&mut self)->Option<u8> {
        for i in self.pos .. 9 {
            if (self.set.0 & (1 << i)) != 0 {
                self.pos = i+1;
                return Some(i)
            }
        }
        self.pos = 9;
        None
    }
}

impl IntoIterator for CandidateSet {
    type Item = u8;
    type IntoIter = CandidateIter;
    fn into_iter(self)->CandidateIter { CandidateIter { set: self, pos: 0 } }
}


impl Grid {
    fn sqr(&self, x: usize, y:usize)->CandidateSet {
        CandidateSet::from_iter(self.0[y*9+    x..y*9+x+3].iter().filter_map(|&opt| opt)) +
        CandidateSet::from_iter(self.0[y*9+x+ 9..y*9+x+12].iter().filter_map(|&opt| opt)) +
        CandidateSet::from_iter(self.0[y*9+x+18..y*9+x+21].iter().filter_map(|&opt| opt))
    }
    
    fn col(&self, x:usize)->CandidateSet {
        CandidateSet::from_iter((0..9).map(|y| &self.0[x+9*y]).filter_map(|&opt| opt))
    }
    
    fn row(&self, y:usize)->CandidateSet {
        CandidateSet::from_iter(self.0[y*9..y*9+9].iter().filter_map(|&opt| opt))
    }
    
    fn free(&self, x:usize, y:usize)->CandidateSet {
        CandidateSet::all() - (self.col(x) + self.row(y) + self.sqr((x/3)*3, (y/3)*3))
    }
    
    fn resolv(&mut self)->bool {
        let i = match self.0.iter().position(Option::is_none) {
            None => return true, // solved
            Some(i) => i
        };
        
        for c in self.free(i%9, i/9) {
            self.0[i] = Some(c);
            if self.resolv() { return true; }
        }
        self.0[i] = None;
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
        let mut grid = [None;81];
        for (i,(g,c)) in grid.iter_mut().zip(s.chars()).enumerate() {
            if ('1'..='9').contains(&c) { *g = Some(c as u8-'1' as u8); }
            else if c != '.' { return Err(ParseGridError { pos: i }) }
        }
        Ok(Grid(grid))
    }
}

impl Display for Grid {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result<(), std::fmt::Error> {
        for g in self.0 {
            write!(f, "{}", match g {
                Some(x) => ('1' as u8 + x) as char,
                None => '.'
            })?;
        }
        Ok(())
    }
}
fn main() -> Result<(), Box<dyn std::error::Error>> {

    let content = fs::read_to_string("grids.txt")?;
    let gg: Vec<&str> = content.lines().take(100).collect();

    let t = std::time::Instant::now();
    for line in gg {
        let mut grid: Grid = line.trim().parse().unwrap();
        grid.resolv();
        println!("{} ", grid);
    }
    println!("Took: {} s", (t.elapsed().as_millis() as f32)/1000.0);
    Ok(())
}
