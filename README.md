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
 ./sudoku.c : the simple algo, with strings (AI translation from java one) (100grids)
  - gcc   : 2.46 seconds (24x, 2.29><2.93)

 ./sudoku.mojo : the simple algo, with strings (100grids)
  - mojo  : 16.42 seconds (12x, 16.09><17.41) <-------------------- (*)

 ./sudoku.js : the simple algo, with strings (AI translation from java one) (100grids)
  - node  : 43.83 seconds (11x, 43.54><45.33)


 ./sudoku.nim : the simple algo, with strings (100grids)
  - nim   : 9.13 seconds (14x, 8.88><9.29)

 ./sudoku.rs : the simple algo, with strings (AI translation from java one) (100grids)
  - rust  : 38.01 seconds (11x, 27.18><47.40)

 ./sudoku.py : the simple algo, with strings (100grids)
  - codon : 20.25 seconds (14x, 20.08><21.90)
  - py311 : 26.2 seconds (14x, 23.51><35.60)
  - py37  : 39.96 seconds (14x, 33.65><48.75)
  - pypy  : 19.01 seconds (14x, 18.48><20.30)

 ./sudoku.java : the simple algo, with strings (100grids)
  - java  : 20.83 seconds (12x, 17.25><27.68)

```

(*) : was 6.65s with `mojo 0.4.0 (9e33b013)` and [source_for_0.4.0](https://github.com/manatlan/sudoku_resolver/blob/mojo_0.4.0/sudoku.mojo), [perf issue](https://github.com/modularml/mojo/issues/1216)

## SPECIALIZED versions, results

The same algo, but with specialized types/structures for the language (to speed up things)

```
 ./sudoku_specialized.mojo : the simple algo, with specialized mojo-types (100grids)
  - mojo  : 0.92 seconds (37x, 0.91><1.07)

 ./sudoku_specialized_parallel.mojo : the simple algo, with specialized types & parallelization (100grids)
  - mojo  : 0.36 seconds (34x, 0.35><0.47)

 ./sudoku_specialized.rs : the simple algo, with ultra-specialized types/api (100grids)
  - rust  : 0.93 seconds (30x, 0.93><1.18)

```

## If you want to tests on your own

You will need, at least, python3 ;-) (it will autodetect compilers/interpreters on your host)
```
$ git clone https://github.com/manatlan/sudoku_resolver.git
$ cd sudoku_resolver
$ chmod +x make.py
$ ./make.py .
...(processing)...
$ ./make.py stats
```
(repeat the `./make.py .` to get accurate results)

see command line [make.py](make.md)

## OPTIMIZED algo

See results on [an optimized algo](optimized) versions. (a better algo)

## EXPERIMENTS results:

See [experimentals](experiments) versions. (just for tests purposes)

