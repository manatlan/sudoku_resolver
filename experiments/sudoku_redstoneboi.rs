#!/usr/bin/rustc -C opt-level=3 -C target-cpu=native experiments/sudoku_redstoneboi.rs -o exe && ./exe

//INFO: using strings (but specialized charset & mutable resolv'str) (100grids)

// from https://www.reddit.com/r/rust/comments/183ex3i/need_help_to_make_a_rust_algo_faster/
// from https://gist.github.com/raffimolero/0cc7f282cf6795d8a8ff1cb69d51d6d0 **REDSTONEBOI**

// from ./sudoku.rs base but :
// "A HashSet of 10 characters is insanely inefficient for the task at hand. It could very well just be an array of 10 bools. I created a new type for this and it dropped the runtime from 44s avg to 17s. I then changed col, row, sqr to return impl 'a + Iterator<Item = char> and removed as many collects as possible to get rid of a bunch of allocations. Then I changed resolv to make only one clone of the given String, and keep mutating it back and forth instead of using format!() which made way too many allocations."
// 38s -> 5.6s

use std::{fs, ops::SubAssign};

struct CharSet([bool; 9]);

impl CharSet {
    fn all() -> Self {
        Self([true; 9])
    }

    fn iter<'a>(&'a self) -> impl 'a + Iterator<Item = char> {
        self.0
            .iter()
            .enumerate()
            .filter_map(|(i, v)| v.then(|| (b'1' + i as u8) as char))
    }
}

impl<T: IntoIterator<Item = char>> SubAssign<T> for CharSet {
    fn sub_assign(&mut self, rhs: T) {
        for c in rhs {
            if c == '.' {
                continue;
            }
            self.0[(c as u8 - b'1') as usize] = false;
        }
    }
}

fn sqr<'a>(g: &'a str, x: usize, y: usize) -> impl 'a + Iterator<Item = char> {
    let x = (x / 3) * 3;
    let y = (y / 3) * 3;
    let i = y * 9 + x;
    g[i..i + 3]
        .chars()
        .chain(g[i + 9..i + 9 + 3].chars())
        .chain(g[i + 18..i + 18 + 3].chars())
}

fn col<'a>(g: &'a str, x: usize) -> impl 'a + Iterator<Item = char> {
    (0..9).map(move |y| g.chars().skip(x + y * 9).next().unwrap())
}

fn row<'a>(g: &'a str, y: usize) -> impl 'a + Iterator<Item = char> {
    g[y * 9..y * 9 + 9].chars()
}

fn free(g: &str, x: usize, y: usize) -> CharSet {
    let mut all_chars: CharSet = CharSet::all();
    all_chars -= row(g, y);
    all_chars -= col(g, x);
    all_chars -= sqr(g, x, y);
    all_chars
}

fn resolv_inner(g: &mut String) -> bool {
    let Some(i) = g.find('.') else { return true };
    for elem in free(g, i % 9, i / 9).iter() {
        let mut buf = [0; 1];
        g.replace_range(i..i + 1, elem.encode_utf8(&mut buf));
        if resolv_inner(g) {
            return true;
        }
        g.replace_range(i..i + 1, ".");
    }
    false
}

fn resolv(g: &str) -> Option<String> {
    let mut g = g.to_owned();
    resolv_inner(&mut g).then(|| g)
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