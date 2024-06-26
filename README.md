Here is the **simplest|minimal|readable** python3 resolver (naive backtracking recursive):

The idea of the repo, is to compare the runtime speed of differents languages. Currently, there a py/mojo/nim/go/java/js/rust versions. So every version implements the same algorithm, without using specialized types provided by the language itself ... and try to resolve the 1956 grids of [grids.txt](grids.txt) (only good/solvable ones, no empty grid) !!!

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
sudoku.go : algo with strings
  - go    : 17.166 seconds (4x, 16.710><17.240)
  
sudoku.java : algo with strings
  - java  : 39.656 seconds (2x, 39.409><39.902)

sudoku.js : algo with strings
  - node  : 41.311 seconds (2x, 39.991><42.631)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 89.145 seconds (6x, 83.489><95.430)

sudoku.nim : algo with strings
  - nim   : 27.555 seconds (2x, 27.019><28.090)

sudoku.py : algo with strings
  - py3   : 88.972 seconds (3x, 88.880><90.797)
  - pypy  : 29.358 seconds (3x, 28.443><31.244)
  - codon : 17.128 seconds (3x, 16.191><17.806)
  - py37  : 138.129 seconds (2x, 137.556><138.701)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 10.357 seconds (4x, 10.197><10.710)
```

(Since v0.5.0, mojo is a lot slower : [issue](https://github.com/modularml/mojo/issues/1216) ... it was a lot faster with 0.4.0)
(mojo v0.6.1 was 73.747 seconds ... so v0.7.0 is a little bit speedier ... but the v24.x are slower ;-( )

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```
specialized/sudoku.mojo : algo with specialized types (use python to read stdin)
  - mojo  : 2.681 seconds (7x, 2.664><2.701)

specialized/sudoku.rs : algo with specialized types
  - rust  : 1.188 seconds (2x, 1.146><1.231)
```


## Context (on my computer)

On my computer (Intel® N100 × 4 / ubuntu 23.10), with versions and command line used:
```
PLATFORM : x86_64/Linux-6.5.0-13-generic-x86_64-with-glibc2.38 with 4 cpus
CPUINFO  : GenuineIntel "Intel(R) N100" (1612.80 bogomips)
MEMINFO  : 16142748 kB

codon : 0.16.3
        /home/manatlan/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.21.1 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 22-ea 2024-03-19
        /usr/bin/javac <file> && /usr/bin/java Sudoku < grids.txt
mojo  : mojo 24.2.0 (c2427bc5)
        /home/manatlan/.modular/pkg/packages.modular.com_mojo/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.0 [Linux: amd64]
        /home/manatlan/.nimble/bin/nim compile -d:danger <file> && ./sudoku < grids.txt
node  : v18.13.0
        /usr/bin/node <file> < grids.txt
py3   : Python 3.11.6
        /usr/bin/python3 -uOO <file> < grids.txt
py37  : Python 3.7.16
        /usr/local/bin/python3.7 -uOO <file> < grids.txt
pypy  : Python 3.9.17 (7.3.12+dfsg-1, Jun 16 2023, 23:19:37)
        /usr/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.75.0 (82e1608df 2023-12-21) (built from a source tarball)
        /usr/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


## If you want to tests on your own

You will need, at least, python3 ;-) (it will autodetect compilers/interpreters on your host)
```bash
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
