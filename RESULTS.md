
# Results from HOST "fv-az570-975"

Here are informations about the host/computer, and languages/versions used for tests:
```
PLATFORM : x86_64/Linux-6.2.0-1016-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.85 bogomips)
MEMINFO  : 16365012 kB

mojo  : mojo 0.5.0 (6e50a738)
        /home/runner/.modular/pkg/packages.modular.com_mojo/bin/mojo run <file>
nim   : Nim Compiler Version 2.0.0 [Linux: amd64]
        /home/runner/.nimble/bin/nim r -d:danger <file>
java  : openjdk 11.0.21 2023-10-17
        /usr/bin/java <file>
node  : v18.18.2
        /usr/local/bin/node <file>
py3   : Python 3.10.12
        /usr/bin/python3 -uOO <file>
rust  : rustc 1.73.0 (cc66ad468 2023-10-03)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o exe && ./exe
gcc   : gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
        /usr/bin/gcc <file> -o exe && ./exe
pypy  : Python 3.9.18 (c5262994620471e725f57d652d78d842270649d6, Sep 27 2023, 13:43:44)
        /opt/hostedtoolcache/PyPy/3.9.18/x64/bin/pypy3 -uOO <file>
codon : 0.16.3
        /home/runner/.codon/bin/codon run -release <file>

```

The goal is to test two algorithm (sudoku backtracking) using different languages, to compare runtime speed.

- The [first](sudoku.py) is simple, and tests only 100 grids.
- The [second](optimized/sudoku.py) is an optimization of the first, and is a lot faster. So it can tests **all 1956 grids** !

## Simple Algo

For the first 100 grids : At each iteration, they will resolve the first hole of the grid, til no holes.
(*specialized* versions use all weapons available in language, while others use string and hashset)
```

sudoku.c : the simple algo, with strings (AI translation from java one) (100grids)
  - gcc   : 3.399 seconds (1x, 3.399><3.399)

sudoku.java : the simple algo, with strings (100grids)
  - java  : 20.893 seconds (1x, 20.893><20.893)

sudoku.js : the simple algo, with strings (AI translation from java one) (100grids)
  - node  : 34.449 seconds (1x, 34.449><34.449)

sudoku.mojo : the simple algo, with strings (100grids)
  - mojo  : 16.305 seconds (1x, 16.305><16.305)

sudoku.nim : the simple algo, with strings (100grids)
  - nim   : 10.377 seconds (1x, 10.377><10.377)

sudoku.py : the simple algo, with strings (100grids)
  - codon : 18.166 seconds (1x, 18.166><18.166)
  - py3   : 41.871 seconds (1x, 41.871><41.871)
  - pypy  : 14.666 seconds (1x, 14.666><14.666)

sudoku.rs : the simple algo, with Strings (as byte[]) (100grids)
  - rust  : 10.645 seconds (1x, 10.645><10.645)

sudoku_specialized.mojo : the simple algo, with specialized types (100grids)
  - mojo  : 2.704 seconds (1x, 2.704><2.704)

sudoku_specialized.rs : the simple algo, with specialized types (100grids)
  - rust  : 11.334 seconds (1x, 11.334><11.334)

sudoku_specialized_parallel.mojo : the simple algo, with specialized types & parallelization (100grids)
  - mojo  : 2.681 seconds (1x, 2.681><2.681)

```

## Optimized Algo

For **all 1956** grids : At each iteration, they will firstly resolve the hole, with minimal choices, of the grid, til no holes.
(*specialized* versions use all weapons available in language, while others use string and hashset)

```

optimized/sudoku.java : the optimized algo, with strings (1956grids)
  - java  : 99.044 seconds (1x, 99.044><99.044)

optimized/sudoku.mojo : the optimized algo, with strings (1956grids)
  - mojo  : 55.903 seconds (1x, 55.903><55.903)

optimized/sudoku.py : the optimized algo, with strings (1956grids)
  - codon : 77.039 seconds (1x, 77.039><77.039)
  - py3   : 148.535 seconds (1x, 148.535><148.535)
  - pypy  : 85.998 seconds (1x, 85.998><85.998)

optimized/sudoku_specialized.mojo : optimized algo, with specialized types (1956grids)
  - mojo  : 3.797 seconds (1x, 3.797><3.797)

optimized/sudoku_specialized.rs : the optimized algo, with specialized types (and readable) (1956grids)
  - rust  : 1.427 seconds (1x, 1.427><1.427)

optimized/sudoku_specialized_parallel.mojo : optimized algo, with specialized types & parallelization (1956grids)
  - mojo  : 2.995 seconds (1x, 2.995><2.995)

```


