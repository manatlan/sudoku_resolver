
# Results from HOST "fv-az1499-185"

Here are informations about the host/computer, and languages/versions used for tests:
```
PLATFORM : x86_64/Linux-6.2.0-1016-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.86 bogomips)
MEMINFO  : 16365020 kB

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
  - gcc   : 2.994 seconds (1x, 2.994><2.994)

sudoku.java : the simple algo, with strings (100grids)
  - java  : 20.138 seconds (1x, 20.138><20.138)

sudoku.js : the simple algo, with strings (AI translation from java one) (100grids)
  - node  : 34.745 seconds (1x, 34.745><34.745)

sudoku.mojo : the simple algo, with strings (100grids)
  - mojo  : 16.594 seconds (1x, 16.594><16.594)

sudoku.nim : the simple algo, with strings (100grids)
  - nim   : 10.225 seconds (1x, 10.225><10.225)

sudoku.py : the simple algo, with strings (100grids)
  - codon : 18.241 seconds (1x, 18.241><18.241)
  - py3   : 31.262 seconds (1x, 31.262><31.262)
  - pypy  : 14.947 seconds (1x, 14.947><14.947)

sudoku.rs : the simple algo, with Strings (as byte[]) (100grids)
  - rust  : 10.869 seconds (1x, 10.869><10.869)

sudoku_specialized.mojo : the simple algo, with specialized types (100grids)
  - mojo  : 2.754 seconds (1x, 2.754><2.754)

sudoku_specialized.rs : the simple algo, with specialized types (100grids)
  - rust  : 1.802 seconds (1x, 1.802><1.802)

sudoku_specialized_parallel.mojo : the simple algo, with specialized types & parallelization (100grids)
  - mojo  : 2.624 seconds (1x, 2.624><2.624)

```

## Optimized Algo

For **all 1956** grids : At each iteration, they will firstly resolve the hole, with minimal choices, of the grid, til no holes.
(*specialized* versions use all weapons available in language, while others use string and hashset)

```

optimized/sudoku.java : the optimized algo, with strings (1956grids)
  - java  : 98.076 seconds (1x, 98.076><98.076)

optimized/sudoku.mojo : the optimized algo, with strings (1956grids)
  - mojo  : 55.439 seconds (1x, 55.439><55.439)

optimized/sudoku.py : the optimized algo, with strings (1956grids)
  - codon : 78.853 seconds (1x, 78.853><78.853)
  - py3   : 132.685 seconds (1x, 132.685><132.685)
  - pypy  : 83.875 seconds (1x, 83.875><83.875)

optimized/sudoku_specialized.mojo : optimized algo, with specialized types (1956grids)
  - mojo  : 3.728 seconds (1x, 3.728><3.728)

optimized/sudoku_specialized.rs : the optimized algo, with specialized types (and readable) (1956grids)
  - rust  : 1.101 seconds (1x, 1.101><1.101)

optimized/sudoku_specialized_parallel.mojo : optimized algo, with specialized types & parallelization (1956grids)
  - mojo  : 2.961 seconds (1x, 2.961><2.961)

```


