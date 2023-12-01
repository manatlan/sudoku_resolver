#!./make.py
//INFO: the simple algo, with Strings (as byte[]) (100grids)

// This version doesn't use "Strings", but "byte[]", because :
// The weapons are not the same because other languages do not have UTF-8 encoded
// strings. So Rust is at huge disadvantage here for no reason. String operations
// that are constant time in other languages take linear time in Rust because it
// tries to handle the complexity of UTF correctly. (https://www.reddit.com/user/ondrejdanek/)
// https://www.reddit.com/r/rust/comments/183ex3i/comment/kapmmub/?utm_source=share&utm_medium=web2x&context=3

// the original with string is here "./experiments/sudoku_original_with_strings_only.rs" (~30s)
// https://github.com/manatlan/sudoku_resolver/pull/11
// thanks @noamtashma & @sammysheep for the fix !

use std::fs;

fn sqr(g: &[u8], x: usize, y: usize) -> impl Iterator<Item = u8> + '_ {
    let x = (x / 3) * 3;
    let y = (y / 3) * 3;
    IntoIterator::into_iter([
        &g[y * 9 + x..y * 9 + x + 3],
        &g[y * 9 + x + 9..y * 9 + x + 12],
        &g[y * 9 + x + 18..y * 9 + x + 21],
    ])
    .flatten()
    .cloned()
}

fn col(g: &[u8], x: usize) -> impl Iterator<Item = u8> + '_ {
    (0..9).map(move |y| g[x + y * 9])
}

fn row(g: &[u8], y: usize) -> impl Iterator<Item = u8> + '_ {
    g[y * 9..y * 9 + 9].iter().copied()
}

// More similar to existing implementations but allocates and does multiple passes
fn free(g: &[u8], x: usize, y: usize) -> impl Iterator<Item = u8> + '_ {
    b"123456789".iter().copied().filter(move |elem| {
        // Iterators consume, so this is necessary for correctness
        let mut t27 = row(g, y).chain(col(g, x)).chain(sqr(g, x, y));
        !t27.any(|c| c == *elem)
    })
}

//-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
// a faster way to make free(), from @sammysheep
//-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
// Avoids allocating by using an iterator and scans in a single pass
fn free_faster(g: &[u8], x: usize, y: usize) -> impl Iterator<Item = u8> + '_ {
    let numbers_found = row(g, y)
        .chain(col(g, x))
        .chain(sqr(g, x, y))
        .fold(0u16, |acc, b| acc | 1u16 << (b - b'0'));

    (1..10u8)
        .filter(move |&b| 1u16 << b & numbers_found == 0)
        .map(|b| b + b'0')
}
//-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

fn resolv(g: &[u8]) -> Option<Vec<u8>> {
    if let Some(i) = g.iter().position(|&c| c == b'.') {
        for free_number in free(g, i % 9, i / 9) {
            let mut new_board = g.to_owned();
            new_board[i] = free_number;
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

    for g in gg {
        if let Some(rg) = resolv(g.as_bytes()) {
            println!("{}", std::str::from_utf8(&rg)?);
        }
    }
    Ok(())
}