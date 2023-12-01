# Results from 'GITHUB' host

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
(*specialized* versions use all weapons available in language, while others use strings only)
```

sudoku.c : the simple algo, with strings (AI translation from java one) (100grids)
  - gcc   : 2.940 seconds (19x, 2.855><3.620)

sudoku.java : the simple algo, with strings (100grids)
  - java  : 7.630 seconds (12x, 7.064><8.945)

sudoku.js : the simple algo, with strings (AI translation from java one) (100grids)
  - node  : 6.878 seconds (12x, 6.794><8.189)

sudoku.mojo : the simple algo, with strings (100grids)
  - mojo  : 16.531 seconds (12x, 16.427><16.868)

sudoku.nim : the simple algo, with strings (100grids)
  - nim   : 7.454 seconds (5x, 7.406><8.282)

sudoku.py : the simple algo, with strings (100grids)
  - codon : 4.892 seconds (12x, 4.800><5.040)
  - py3   : 22.253 seconds (12x, 21.968><24.121)
  - pypy  : 4.904 seconds (12x, 4.386><5.684)

sudoku.rs : the simple algo, with Strings (as byte[]) (100grids)
  - rust  : 2.685 seconds (1x, 2.685><2.685)

sudoku_specialized.mojo : the simple algo, with specialized types (100grids)
  - mojo  : 2.760 seconds (19x, 2.724><2.882)

sudoku_specialized.rs : the simple algo, with specialized types (100grids)
  - rust  : 0.923 seconds (1x, 0.923><0.923)

sudoku_specialized_parallel.mojo : the simple algo, with specialized types & parallelization (100grids)
  - mojo  : 2.525 seconds (19x, 2.471><2.679)

```

## Optimized Algo

For **all 1956** grids : At each iteration, they will firstly resolve the hole, with minimal choices, of the grid, til no holes.
(*specialized* versions use all weapons available in language, while others use strings only)

```

optimized/sudoku.java : the optimized algo, with strings (1956grids)
  - java  : 28.633 seconds (12x, 27.687><29.469)

optimized/sudoku.js : the optimized algo, with strings (AI translation from java one) (1956grids)
  - node  : 29.033 seconds (5x, 28.807><29.316)

optimized/sudoku.mojo : the optimized algo, with strings (1956grids)
  - mojo  : 55.946 seconds (19x, 55.438><58.135)

optimized/sudoku.nim : the optimized algo, with strings (1956grids)
  - nim   : 25.515 seconds (5x, 25.163><25.719)

optimized/sudoku.py : the optimized algo, with strings (1956grids)
  - codon : 20.857 seconds (12x, 20.719><21.095)
  - py3   : 122.759 seconds (12x, 121.566><123.468)
  - pypy  : 33.809 seconds (12x, 33.619><34.057)

optimized/sudoku_specialized.mojo : optimized algo, with specialized types (1956grids)
  - mojo  : 3.757 seconds (19x, 3.726><3.806)

optimized/sudoku_specialized.rs : the optimized algo, with specialized types (and readable) (1956grids)
  - rust  : 0.988 seconds (1x, 0.988><0.988)

optimized/sudoku_specialized_parallel.mojo : optimized algo, with specialized types & parallelization (1956grids)
  - mojo  : 2.936 seconds (19x, 2.904><2.979)

```


