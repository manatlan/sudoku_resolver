# Host infos
```
PLATFORM : x86_64/Linux-6.2.0-1016-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.86 bogomips)
MEMINFO  : 16365020 kB
```

With:
 - codon : 0.16.3
 - gcc   : gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
 - java  : openjdk 11.0.21 2023-10-17
 - mojo  : mojo 0.5.0 (6e50a738)
 - nim   : Nim Compiler Version 2.0.0 [Linux: amd64]
 - node  : v18.18.2
 - py3   : Python 3.10.12
 - pypy  : Python 3.9.18 (c5262994620471e725f57d652d78d842270649d6, Sep 27 2023, 13:43:44)
 - rust  : rustc 1.73.0 (cc66ad468 2023-10-03)

# Results
```
./sudoku.c : the simple algo, with strings (AI translation from java one) (100grids)
  - gcc   : 2.898 (1x, 2.898><2.898)

./sudoku.java : the simple algo, with strings (100grids)
  - java  : 19.871 (1x, 19.871><19.871)

./sudoku.js : the simple algo, with strings (AI translation from java one) (100grids)
  - node  : 34.564 (1x, 34.564><34.564)

./sudoku.mojo : the simple algo, with strings (100grids)
  - mojo  : 15.991 (1x, 15.991><15.991)

./sudoku.nim : the simple algo, with strings (100grids)
  - nim   : 9.170 (1x, 9.170><9.170)

./sudoku.py : the simple algo, with strings (100grids)
  - codon : 16.068 (1x, 16.068><16.068)
  - py3   : 38.280 (1x, 38.280><38.280)
  - pypy  : 14.329 (1x, 14.329><14.329)

./sudoku.rs : the simple algo, with Strings (as byte[]) (100grids)
  - rust  : 7.752 (1x, 7.752><7.752)

./sudoku_specialized.mojo : the simple algo, with specialized types (100grids)
  - mojo  : 0.738 (1x, 0.738><0.738)

./sudoku_specialized.rs : the simple algo, with specialized types (100grids)
  - rust  : 0.586 (1x, 0.586><0.586)

./sudoku_specialized_parallel.mojo : the simple algo, with specialized types & parallelization (100grids)
  - mojo  : 0.396 (1x, 0.396><0.396)

optimized/sudoku.java : the optimized algo, with strings (1956grids)
  - java  : 100.932 (1x, 100.932><100.932)

optimized/sudoku.mojo : the optimized algo, with strings (1956grids)
  - mojo  : 55.375 (1x, 55.375><55.375)

optimized/sudoku.py : the optimized algo, with strings (1956grids)
  - codon : 74.510 (1x, 74.510><74.510)
  - py3   : 147.016 (1x, 147.016><147.016)
  - pypy  : 93.074 (1x, 93.074><93.074)

optimized/sudoku_specialized.mojo : optimized algo, with specialized types (1956grids)
  - mojo  : 1.735 (1x, 1.735><1.735)

optimized/sudoku_specialized.rs : the optimized algo, with specialized types (and readable) (1956grids)
  - rust  : 0.643 (1x, 0.643><0.643)

optimized/sudoku_specialized_parallel.mojo : optimized algo, with specialized types & parallelization (1956grids)
  - mojo  : 0.876 (1x, 0.876><0.876)

```
