# Results from HOST 'fv-az973-395'

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.2.0-1016-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.86 bogomips)
MEMINFO  : 16365020 kB

codon : 0.16.3
        /home/runner/.codon/bin/codon run -release <file>
gcc   : gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
        /usr/bin/gcc <file> -o exe && ./exe
java  : openjdk 11.0.21 2023-10-17
        /usr/bin/java <file>
mojo  : mojo 0.5.0 (6e50a738)
        /home/runner/.modular/pkg/packages.modular.com_mojo/bin/mojo run <file>
nim   : Nim Compiler Version 2.0.0 [Linux: amd64]
        /home/runner/.nimble/bin/nim r -d:danger <file>
node  : v18.18.2
        /usr/local/bin/node <file>
py3   : Python 3.10.12
        /usr/bin/python3 -uOO <file>
pypy  : Python 3.9.18 (c5262994620471e725f57d652d78d842270649d6, Sep 27 2023, 13:43:44)
        /opt/hostedtoolcache/PyPy/3.9.18/x64/bin/pypy3 -uOO <file>
rust  : rustc 1.74.0 (79e9716c9 2023-11-13)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o exe && ./exe

```

The goal is to test two algorithms (sudoku backtracking) using different languages, to compare runtime speed.

- The [first](sudoku.py) is a **simple algo**, and solves only 100 grids.
- The [second](optimized/sudoku.py) is an **optimized algo** and is a lot faster. So it can solve **all 1956 grids** !

## Simple Algo

For the first 100 grids : At each iteration, they will resolve the first hole of the grid, til no holes.
(*specialized* versions use all weapons available in language, while others use string and hashset)
```

sudoku.c : the simple algo, with strings (AI translation from java one) (100grids)
  - gcc   : 2.999 seconds (9x, 2.909><3.620)

sudoku.java : the simple algo, with strings (100grids)
  - java  : 8.021 seconds (2x, 7.097><8.945)

sudoku.js : the simple algo, with strings (AI translation from java one) (100grids)
  - node  : 7.538 seconds (2x, 6.887><8.189)

sudoku.mojo : the simple algo, with strings (100grids)
  - mojo  : 16.471 seconds (2x, 16.438><16.504)

sudoku.nim : the simple algo, with strings (100grids)
  - nim   : 8.091 seconds (2x, 7.978><8.203)

sudoku.py : the simple algo, with strings (100grids)
  - codon : 5.033 seconds (2x, 5.026><5.040)
  - py3   : 22.165 seconds (2x, 22.163><22.168)
  - pypy  : 4.929 seconds (2x, 4.888><4.970)

sudoku.rs : the simple algo, with Strings (as byte[]) (100grids)
  - rust  : 18.994 seconds (1x, 18.994><18.994)

sudoku_specialized.mojo : the simple algo, with specialized types (100grids)
  - mojo  : 2.760 seconds (9x, 2.739><2.882)

sudoku_specialized.rs : the simple algo, with specialized types (100grids)
  - rust  : 1.334 seconds (1x, 1.334><1.334)

sudoku_specialized_parallel.mojo : the simple algo, with specialized types & parallelization (100grids)
  - mojo  : 2.610 seconds (9x, 2.489><2.679)

```

## Optimized Algo

For **all 1956** grids : At each iteration, they will firstly resolve the hole, with minimal choices, of the grid, til no holes.
(*specialized* versions use all weapons available in language, while others use string and hashset)

```

optimized/sudoku.java : the optimized algo, with strings (1956grids)
  - java  : 28.846 seconds (2x, 28.806><28.886)

optimized/sudoku.mojo : the optimized algo, with strings (1956grids)
  - mojo  : 56.016 seconds (9x, 55.438><58.135)

optimized/sudoku.py : the optimized algo, with strings (1956grids)
  - codon : 20.877 seconds (2x, 20.831><20.923)
  - py3   : 122.186 seconds (2x, 121.566><122.806)
  - pypy  : 33.967 seconds (2x, 33.903><34.030)

optimized/sudoku_specialized.mojo : optimized algo, with specialized types (1956grids)
  - mojo  : 3.757 seconds (9x, 3.726><3.769)

optimized/sudoku_specialized.rs : the optimized algo, with specialized types (and readable) (1956grids)
  - rust  : 1.366 seconds (1x, 1.366><1.366)

optimized/sudoku_specialized_parallel.mojo : optimized algo, with specialized types & parallelization (1956grids)
  - mojo  : 2.955 seconds (9x, 2.926><2.971)

```


