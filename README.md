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
PLATFORM : x86_64/Linux-6.5.0-13-generic-x86_64-with-glibc2.38 with 4 cpus
CPUINFO  : GenuineIntel "Intel(R) N100" (1612.80 bogomips)
MEMINFO  : 16142748 kB

codon : 0.16.3
        /home/manatlan/.codon/bin/codon run -release <file>
gcc   : gcc (Ubuntu 13.2.0-4ubuntu3) 13.2.0
        /usr/bin/gcc <file> -o exe && ./exe
java  : openjdk 22-ea 2024-03-19
        /usr/bin/java <file>
mojo  : mojo 0.5.0 (6e50a738)
        /home/manatlan/.modular/pkg/packages.modular.com_mojo/bin/mojo run <file>
nim   : Nim Compiler Version 2.0.0 [Linux: amd64]
        /home/manatlan/.nimble/bin/nim r -d:danger <file>
node  : v18.13.0
        /usr/bin/node <file>
py3   : Python 3.11.6
        /usr/bin/python3 -uOO <file>
py37  : Python 3.7.16
        /usr/local/bin/python3.7 -uOO <file>
pypy  : Python 3.9.17 (7.3.12+dfsg-1, Jun 16 2023, 23:19:37)
        /usr/bin/pypy3 -uOO <file>
rust  : rustc 1.71.1 (eb26296b5 2023-08-03) (built from a source tarball)
        /usr/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o exe && ./exe
```


## Simple version, results

The 1/1 implementations of the py version, in each language (using strings)

``` 
sudoku.c : the simple algo, with strings (AI translation from java one) (100grids)
  - gcc   : 2.488 seconds (5x, 2.479><2.583)

sudoku.java : the simple algo, with strings (100grids)
  - java  : 21.090 seconds (5x, 20.815><26.354)

sudoku.js : the simple algo, with strings (AI translation from java one) (100grids)
  - node  : 44.653 seconds (5x, 43.692><49.268)

sudoku.mojo : the simple algo, with strings (100grids)
  - mojo  : 16.564 seconds (5x, 16.249><18.935) <-------------------- (*)

sudoku.nim : the simple algo, with strings (100grids)
  - nim   : 9.255 seconds (5x, 9.182><9.718)

sudoku.py : the simple algo, with strings (100grids)
  - py3   : 22.005 seconds (5x, 20.518><31.651)
  - pypy  : 17.906 seconds (5x, 17.702><19.967)
  - codon : 22.923 seconds (5x, 22.621><26.154)
  - py37  : 39.988 seconds (5x, 33.920><50.226)

sudoku.rs : the simple algo, with Strings (as byte[]) (100grids)
  - rust  : 10.687 seconds (5x, 6.494><10.894)

```

(*) : was 6.65s with `mojo 0.4.0 (9e33b013)` and [source_for_0.4.0](https://github.com/manatlan/sudoku_resolver/blob/mojo_0.4.0/sudoku.mojo), [perf issue](https://github.com/modularml/mojo/issues/1216)

## SPECIALIZED versions, results

The same algo, but with specialized types/structures for the language (to speed up things)

```
sudoku_specialized.mojo : the simple algo, with specialized types (100grids)
  - mojo  : 1.102 seconds (5x, 1.064><1.196)

sudoku_specialized.rs : the simple algo, with specialized types (100grids)
  - rust  : 1.171 seconds (5x, 1.166><1.290)

sudoku_specialized_parallel.mojo : the simple algo, with specialized types & parallelization (100grids)
  - mojo  : 0.493 seconds (5x, 0.484><0.567)
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

## Auto tests on github host

All nights: a github's action automatize the tests, and produce results in [Results Page](RESULTS.md).

## OPTIMIZED algo

See results on [an optimized algo](optimized) versions. (a better algo)

## EXPERIMENTS results:

See [experimentals](experiments) versions. (just for tests purposes)

