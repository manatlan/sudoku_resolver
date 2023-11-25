#!./make.py
//INFO: the simple algo, with strings (AI translation from java one) (100grids)
use std::{collections::HashSet, fs};

fn sqr(g: &str, x: usize, y: usize) -> String {
    let x = (x / 3) * 3;
    let y = (y / 3) * 3;
    let i = y * 9 + x;
    g[i..i + 3]
        .chars()
        .chain(g[i + 9..i + 9 + 3].chars())
        .chain(g[i + 18..i + 18 + 3].chars())
        .collect()
}

fn col(g: &str, x: usize) -> String {
    (0..9)
        .map(move |y| {
            let i = x + y * 9;
            g[i..i + 1].chars().next().unwrap()
        })
        .collect()
}

fn row(g: &str, y: usize) -> String {
    g[y * 9..y * 9 + 9].chars().collect()
}

fn freeset(g: &str) -> HashSet<char> {
    let all_digits: HashSet<char> = "123456789".chars().collect();
    let s: HashSet<char> = g.chars().collect();
    all_digits.difference(&s).cloned().collect()
}

fn free(g: &str, x: usize, y: usize) -> HashSet<char> {
    let row_chars = row(g, y);
    let col_chars = col(g, x);
    let sqr_chars = sqr(g, x, y);
    let mut all_chars: HashSet<char> = HashSet::new();
    all_chars.extend(row_chars.chars());
    all_chars.extend(col_chars.chars());
    all_chars.extend(sqr_chars.chars());
    freeset(&all_chars.iter().collect::<String>())
}

fn resolv(g: String) -> Option<String> {
    if let Some(i) = g.find('.') {
        for elem in free(&g, i % 9, i / 9) {
            if let Some(ng) = resolv(format!("{}{}{}", &g[..i], elem, &g[i + 1..])) {
                return Some(ng);
            }
        }
        None
    } else {
        Some(g.to_string())
    }
}
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let content = fs::read_to_string("grids.txt")?;
    let gg: Vec<&str> = content.lines().take(100).collect();

    let t = std::time::Instant::now();
    for g in gg {
        if let Some(rg) = resolv(g.to_owned()) {
            if rg.chars().any(|c| c == '.') {
                panic!("not resolved ?!");
            }
            println!("{}", rg);
        }
    }
    println!("Took: {} s", (t.elapsed().as_millis() as f32) / 1000.0);
    Ok(())
}