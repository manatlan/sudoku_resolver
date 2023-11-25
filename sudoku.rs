#!./make.py
//INFO: the simple algo, with strings (AI translation from java one) (100grids)
use std::{collections::HashSet, fs};

// TIP from u/Feeling-Departure-4 :
// This is all ASCII, so you can use as_bytes(), then you iterate using a simple iter() instead of chars(). For byte characters and strings, just use a prefix: b"0123456789" or b'.'. The function signature will use &[u8] instead of &str.
// Using UTF-8 will slow it down among other things mentioned.
// see https://www.reddit.com/r/rust/comments/183ex3i/comment/kapb8sj/?utm_source=share&utm_medium=web2x&context=3

fn sqr(g: &[u8], x: usize, y: usize) -> Vec<u8> {
    let x = (x / 3) * 3;
    let y = (y / 3) * 3;
    let i = y * 9 + x;
    [&g[i..i + 3], &g[i + 9..i + 9 + 3], &g[i + 18..i + 18 + 3]].concat()
}

fn col(g: &[u8], x: usize) -> Vec<u8> {
    (0..9).map(|y| g[x + y * 9]).collect()
}

fn row(g: &[u8], y: usize) -> &[u8] {
    &g[y * 9..y * 9 + 9]
}

fn freeset(g: &HashSet<u8>) -> Vec<u8> {
    let all_digits: HashSet<u8> = b"123456789".iter().copied().collect();
    all_digits.difference(g).copied().collect()
}

fn free(g: &[u8], x: usize, y: usize) -> Vec<u8> {
    let row_bytes = row(g, y);
    let col_bytes = col(g, x);
    let sqr_bytes = sqr(g, x, y);
    let mut all_bytes: HashSet<u8> = HashSet::new();
    all_bytes.extend(row_bytes.iter());
    all_bytes.extend(col_bytes.iter());
    all_bytes.extend(sqr_bytes.iter());
    freeset(&all_bytes)
}

fn resolv(g: &[u8]) -> Option<Vec<u8>> {
    if let Some(i) = g.iter().position(|&c| c == b'.') {
        for elem in free(g, i % 9, i / 9) {
            let mut new_board = g.to_owned();
            new_board[i] = elem;
            if let Some(ng) = resolv(&new_board) {
                return Some(ng);
            }
        }
        None
    } else {
        Some(g.to_owned())
    }
}
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let content = fs::read_to_string("grids.txt")?;
    let gg: Vec<&str> = content.lines().take(100).collect();

    let t = std::time::Instant::now();
    for g in gg {
        if let Some(rg) = resolv(g.as_bytes()) {
            if rg.iter().any(|c| *c == b'.') {
                panic!("not resolved ?!");
            }
            println!("{}", std::str::from_utf8(&rg)?);
        }
    }
    println!("Took: {} s", (t.elapsed().as_millis() as f32) / 1000.0);
    Ok(())
}
