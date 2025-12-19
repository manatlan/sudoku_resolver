Here is the **simplest|minimal|readable** python3 resolver (naive backtracking recursive):

The idea of the repo, is to compare the runtime speed of differents languages. Currently, there a c/py/mojo/nim/go/java/js/rust versions. So every version implements the same algorithm, without using specialized types provided by the language itself ... and try to resolve the 1956 grids of [grids.txt](grids.txt) (only good/solvable ones, no empty grid) !!!

Here is the algo:

```python
sqr   = lambda g,x,y: g[y*9+x:y*9+x+3] + g[y*9+x+9:y*9+x+12] + g[y*9+x+18:y*9+x+21]
col   = lambda g,x:   g[x::9]
row   = lambda g,y:   g[y*9:y*9+9]
free  = lambda g,x,y: set("123456789") - set(col(g,x) + row(g,y) + sqr(g,(x//3)*3,(y//3)*3))

def resolv(g):
    # search holes with less choices 
    holes={}
    for i in range(81):
        if g[i]==".":
            holes[i]=free(g,i % 9, i // 9)
            if len(holes[i])==1: break  # can't beat that (just one choice)
    if holes: 
        # try the hole with minimal choices
        idx,avails = sorted( holes.items() , key=lambda x: len(x[1])).pop(0)
        for c in avails:
            ng = resolv( g[:idx] + c + g[idx+1:] )
            if ng: return ng
    else:
        # no holes -> it's resolved
        return g
```
**note** : all `free()` method implem; use a string mechanism to not use a `set` type (because it's not available in all languages (_same weapons_))

## Regular Results

``` 
sudoku.c : algo with strings (made by gemini3 from py version)
  - c     : 2.946 seconds (6x, 2.923><3.018)

sudoku.go : algo with strings
  - go    : 17.127 seconds (1x, 17.127><17.127)

sudoku.java : algo with strings
  - java  : 35.992 seconds (1x, 35.992><35.992)

sudoku.js : algo with strings
  - node  : 33.953 seconds (1x, 33.953><33.953)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 26.120 seconds (6x, 24.287><30.971)

sudoku.nim : algo with strings
  - nim   : 27.392 seconds (1x, 27.392><27.392)

sudoku.php : algo with strings
  - php   : 80.259 seconds (2x, 79.189><81.328)

sudoku.py : algo with strings
  - py3   : 84.969 seconds (1x, 84.969><84.969)
  - pypy  : 26.574 seconds (1x, 26.574><26.574)
  - codon : 16.845 seconds (6x, 16.191><17.806)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 14.756 seconds (3x, 14.576><14.812)
```


## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```
specialized/sudoku.go : algo with arrays (optimized by copilot)
  - go    : 3.178 seconds (4x, 3.149><3.223)

specialized/sudoku.nim : algo with specialized types using bitsets (optimized by copilot)
  - nim   : 1.149 seconds (4x, 1.138><1.233)

specialized/sudoku.py : algo with specialized types/logics (optimized by copilot)
  - py3   : 15.508 seconds (2x, 15.111><15.904)
  - codon : 0.959 seconds (2x, 0.922><0.997)
  - pypy  : 1.679 seconds (2x, 1.640><1.717)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.868 seconds (5x, 0.810><0.878)
```


## Context (on my computer)

On my computer (Intel® N100 × 4 / ubuntu 23.10), with versions and command line used:
```
PLATFORM : x86_64/Linux-6.14.0-37-generic-x86_64-with-glibc2.39 with 4 cpus
CPUINFO  : GenuineIntel "Intel(R) N100" (1612.80 bogomips)
MEMINFO  : 16152444 kB

c     : gcc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0
        /usr/bin/gcc -O3 <file> -o ./sudoku && ./sudoku < grids.txt
codon : 0.16.3
        /home/manatlan/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.22.2 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 17.0.17 2025-10-21
        /usr/bin/javac -d . <file> && /usr/bin/java Sudoku < grids.txt
mojo  : Mojo 0.25.7.0 (e5af2b2f)
        /home/manatlan/Documents/python/sudoku_resolver/.venv/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.0 [Linux: amd64]
        /home/manatlan/.nimble/bin/nim compile -d:danger -o:sudoku <file> && ./sudoku < grids.txt
node  : v22.19.0
        /home/manatlan/.nvm/versions/node/v22.19.0/bin/node <file> < grids.txt
php   : PHP 8.3.6 (cli) (built: Jul 14 2025 18:30:55) (NTS)
        /usr/bin/php <file> < grids.txt
py3   : Python 3.12.3
        /home/manatlan/Documents/python/sudoku_resolver/.venv/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.18 (7.3.15+dfsg-1build3, Apr 01 2024, 03:12:48)
        /usr/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.90.0 (1159e78c4 2025-09-14)
        /usr/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt
```


## If you want to tests on your own

You will need, at least, python3 ;-) (it will autodetect compilers/interpreters on your host)
```bash
$ git clone https://github.com/manatlan/sudoku_resolver.git
$ cd sudoku_resolver
$ uv sync
$ uv run ./make.py .
...(processing)...
$ uv run ./make.py stats
```
(repeat the `uv run ./make.py .` to get accurate results)

see command line [make.py](make.md)

## Auto tests on github host

All nights: a github's action automatize the tests, and produce results in [Results Page](RESULTS.md).
