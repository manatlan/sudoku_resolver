Here is the **simplest|minimal|readable** python3 resolver (naive backtracking, recursive):

```python
sqr   = lambda g,x,y: g[y*9+x:y*9+x+3] + g[y*9+x+9:y*9+x+12] + g[y*9+x+18:y*9+x+21]
col   = lambda g,x:   g[x::9]
row   = lambda g,y:   g[y*9:y*9+9]
free  = lambda g,x,y: set("123456789") - set(col(g,x) + row(g,y) + sqr(g,(x//3)*3,(y//3)*3))

def resolv(g):
    i=g.find(".")
    if i>=0:
        for elem in free(g,i%9,i//9):
            ng=resolv( g[:i] + elem + g[i+1:] )
            if ng: return ng
    else:
        return g
```


Some grids are available in `grids.txt` (a grid by line of 81 chars, empty cases are `.`)

The idea of the repo, is to compare differents languages at "run times". Currently, there a c/mojo/nim/java/js/rust versions. So every version implements the same algorithm, without using specials optimisations provided by the language itself ... and try to resolve the **first 100 grids** !!!

## Context (on my computer)

On my computer (Intel® N100 × 4 / ubuntu 23.10), with versions and command line used:
```
 * codon : 0.16.3
           $ /home/manatlan/.codon/bin/codon run -release <source>
 * gcc   : gcc (Ubuntu 13.2.0-4ubuntu3) 13.2.0
           $ /usr/bin/gcc <source> -o exe && ./exe
 * java  : openjdk 22-ea 2024-03-19
           $ /usr/bin/java <source>
 * mojo  : mojo 0.5.0 (6e50a738)
           $ /home/manatlan/.modular/pkg/packages.modular.com_mojo/bin/mojo run <source>
 * nim   : Nim Compiler Version 2.0.0 [Linux: amd64]
           $ /home/manatlan/.nimble/bin/nim r -d:danger <source>
 * node  : v18.13.0
           $ /usr/bin/node <source>
 * py311 : Python 3.11.6
           $ /usr/bin/python3.11 -uOO <source>
 * py37  : Python 3.7.16
           $ /usr/local/bin/python3.7 -uOO <source>
 * pypy  : Python 3.10.13 (f1607341da97ff5a1e93430b6e8c4af0ad1aa019, Sep 28 2023, 05:41:26)
           $ /home/manatlan/Téléchargements/pypy3.10-v7.3.13-linux64/bin/pypy3 -uOO <source>
 * rust  : rustc 1.71.1 (eb26296b5 2023-08-03) (built from a source tarball)
           $ /usr/bin/rustc -C opt-level=3 -C target-cpu=native <source> -o exe && ./exe
```


## Simple version, results

The 1/1 implementations of the py version, in each language (using strings)

```
sudoku.c (the simple algo, with strings (AI translation from java one))
 - gcc   : 2.43 seconds

sudoku.java (the simple algo, with strings)
 - java  : 20.14 seconds

sudoku.js (the simple algo, with strings (AI translation from java one))
 - node  : 44.49 seconds

sudoku.mojo (the simple algo, with strings)
 - mojo  : 16.37 seconds (*)

sudoku.nim (the simple algo, with strings)
 - nim   : 9.12 seconds

sudoku.py (the simple algo, with strings)
 - pypy  : 18.71 seconds
 - codon : 20.79 seconds
 - py311 : 26.56 seconds
 - py37  : 39.74 seconds

sudoku.rs (the simple algo, with strings (AI translation from java one))
 - rust  : 37.49 seconds
```

(*) : was 6.65s with `mojo 0.4.0 (9e33b013)` and [source_for_0.4.0](https://github.com/manatlan/sudoku_resolver/blob/mojo_0.4.0/sudoku.mojo), [perf issue](https://github.com/modularml/mojo/issues/1216)

## SPECIALIZED versions, results

The same algo, but with specialized types/structures for the language (to speed up things)

```
sudoku_specialized.mojo (the simple algo, with specialized mojo-types)
 - mojo  : 0.88 seconds

sudoku_specialized_parallel.mojo (the simple algo, with specialized types & parallelization)
 - mojo  : 0.36 seconds (7tests 0.34<0.39)

sudoku_specialized.rs (the simple algo, with ultra-specialized types/api)
 - rust  : 0.96 seconds
```

## If you want to tests on your own

You will need, at least, python3 ;-) (it will autodetect compilers/interpreters on your host)
```
$ git clone https://github.com/manatlan/sudoku_resolver.git
$ cd sudoku_resolver
$ chmod +x make.py
$ ./make.py .
...(processing)...
$ ./make.py hstats
```
(repeat the `./make.py .` to get accurate results)

see command line [make.py](make.md)

## OPTIMIZED algo

See results on [an optimized algo](optimized) versions. (a better algo)

## EXPERIMENTS results:

See [experimentals](experiments) versions. (just for tests purposes)

