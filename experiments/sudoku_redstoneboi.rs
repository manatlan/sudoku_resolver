#!/usr/bin/rustc -C opt-level=3 -C target-cpu=native experiments/sudoku_redstoneboi.rs -o exe && ./exe

//INFO: using strings (but specialized charset & mutable resolv'str) (100grids)

// from https://www.reddit.com/r/rust/comments/183ex3i/need_help_to_make_a_rust_algo_faster/
// from https://gist.github.com/raffimolero/0cc7f282cf6795d8a8ff1cb69d51d6d0 **REDSTONEBOI**

// from ./sudoku.rs base but :
// "A HashSet of 10 characters is insanely inefficient for the task at hand. It could very well just be an array of 10 bools. I created a new type for this and it dropped the runtime from 44s avg to 17s. I then changed col, row, sqr to return impl 'a + Iterator<Item = char> and removed as many collects as possible to get rid of a bunch of allocations. Then I changed resolv to make only one clone of the given String, and keep mutating it back and forth instead of using format!() which made way too many allocations."
// 38s -> 8s


use std::{fs, ops::Neg};

#[derive(Default)]
struct CharSet([bool; 10]);

impl CharSet {
    fn new() -> Self {
        Self::default()
    }

    fn extend(&mut self, iter: impl IntoIterator<Item = char>) {
        for c in iter {
            let i = if c == '.' { 0 } else { c as u8 - b'0' };
            self.0[i as usize] = true;
        }
    }

    fn iter<'a>(&'a self) -> impl 'a + Iterator<Item = char> {
        self.0.iter().enumerate().filter_map(|(i, v)| {
            v.then(|| {
                if i == 0 {
                    '.'
                } else {
                    (b'0' + i as u8) as char
                }
            })
        })
    }
}

impl Neg for CharSet {
    type Output = Self;

    fn neg(mut self) -> Self::Output {
        for c in self.0.iter_mut() {
            *c ^= true;
        }
        self
    }
}

fn sqr<'a>(g: &'a str, x: usize, y: usize) -> impl 'a + Iterator<Item = char> {
    let x = (x / 3) * 3;
    let y = (y / 3) * 3;
    g.chars()
        .skip(y * 9 + x)
        .take(3)
        .chain(g.chars().skip(y * 9 + x + 9).take(3))
        .chain(g.chars().skip(y * 9 + x + 18).take(3))
}

fn col<'a>(g: &'a str, x: usize) -> impl 'a + Iterator<Item = char> {
    (0..9).map(move |y| g.chars().skip(x + y * 9).next().unwrap())
}

fn row<'a>(g: &'a str, y: usize) -> impl 'a + Iterator<Item = char> {
    g.chars().skip(y * 9).take(9)
}

fn free(g: &str, x: usize, y: usize) -> CharSet {
    let row_chars = row(g, y);
    let col_chars = col(g, x);
    let sqr_chars = sqr(g, x, y);
    let mut all_chars: CharSet = CharSet::new();
    all_chars.extend(row_chars);
    all_chars.extend(col_chars);
    all_chars.extend(sqr_chars);
    -all_chars
}

fn resolv_inner(g: &mut String) -> bool {
    if let Some(i) = g.find('.') {
        for elem in free(g, i % 9, i / 9).iter() {
            let mut buf = [0; 4];
            g.replace_range(i..i + 1, elem.encode_utf8(&mut buf));
            if resolv_inner(g) {
                return true;
            }
            g.replace_range(i..i + 1, ".");
        }
        false
    } else {
        true
    }
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