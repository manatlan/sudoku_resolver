# Results from HOST 'fv-az735-733'

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.2.0-1016-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.85 bogomips)
MEMINFO  : 16365012 kB

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
rust  : rustc 1.73.0 (cc66ad468 2023-10-03)
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
  - gcc   : 2.940 seconds (7x, 2.909><3.251)

sudoku.java : the simple algo, with strings (100grids)
  - java  : 23.442 seconds (7x, 20.623><24.874)

sudoku.js : the simple algo, with strings (AI translation from java one) (100grids)
  - node  : 34.851 seconds (7x, 34.310><35.681)

sudoku.mojo : the simple algo, with strings (100grids)
  - mojo  : 16.419 seconds (7x, 16.335><16.679)

sudoku.nim : the simple algo, with strings (100grids)
  - nim   : 10.129 seconds (7x, 10.079><10.367)

sudoku.py : the simple algo, with strings (100grids)
  - codon : 18.152 seconds (7x, 17.994><18.366)
  - py3   : 32.492 seconds (7x, 27.570><43.309)
  - pypy  : 15.089 seconds (7x, 14.470><15.593)

sudoku.rs : the simple algo, with Strings (as byte[]) (100grids)
  - rust  : 9.808 seconds (7x, 8.718><12.356)

sudoku_specialized.mojo : the simple algo, with specialized types (100grids)
  - mojo  : 2.755 seconds (7x, 2.739><2.788)

sudoku_specialized.rs : the simple algo, with specialized types (100grids)
  - rust  : 1.716 seconds (7x, 0.904><12.450)

sudoku_specialized_parallel.mojo : the simple algo, with specialized types & parallelization (100grids)
  - mojo  : 2.630 seconds (7x, 2.489><2.679)

```

## Optimized Algo

For **all 1956** grids : At each iteration, they will firstly resolve the hole, with minimal choices, of the grid, til no holes.
(*specialized* versions use all weapons available in language, while others use string and hashset)

```

optimized/sudoku.java : the optimized algo, with strings (1956grids)
  - java  : 99.072 seconds (7x, 92.839><103.084)

optimized/sudoku.mojo : the optimized algo, with strings (1956grids)
  - mojo  : 55.946 seconds (7x, 55.438><58.135)

optimized/sudoku.py : the optimized algo, with strings (1956grids)
  - codon : 77.227 seconds (7x, 77.099><77.815)
  - py3   : 154.159 seconds (7x, 143.872><179.307)
  - pypy  : 86.857 seconds (7x, 85.558><90.672)

optimized/sudoku_specialized.mojo : optimized algo, with specialized types (1956grids)
  - mojo  : 3.757 seconds (7x, 3.726><3.769)

optimized/sudoku_specialized.rs : the optimized algo, with specialized types (and readable) (1956grids)
  - rust  : 1.047 seconds (7x, 1.000><1.299)

optimized/sudoku_specialized_parallel.mojo : optimized algo, with specialized types & parallelization (1956grids)
  - mojo  : 2.944 seconds (7x, 2.926><2.971)

```


