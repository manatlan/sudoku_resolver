# Host infos
```
PLATFORM : x86_64/Linux-6.2.0-1016-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.84 bogomips)
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
  - gcc   : 2.832 (1x, 2.832><2.832)

./sudoku.java : the simple algo, with strings (100grids)
  - java  : 20.707 (1x, 20.707><20.707)

./sudoku.js : the simple algo, with strings (AI translation from java one) (100grids)
  - node  : 34.160 (1x, 34.160><34.160)

./sudoku.mojo : the simple algo, with strings (100grids)
  - mojo  : 16.032 (1x, 16.032><16.032)

./sudoku.nim : the simple algo, with strings (100grids)
  - nim   : 9.114 (1x, 9.114><9.114)

./sudoku.py : the simple algo, with strings (100grids)
  - codon : 15.924 (1x, 15.924><15.924)
  - py3   : 36.911 (1x, 36.911><36.911)
  - pypy  : 14.484 (1x, 14.484><14.484)

./sudoku.rs : the simple algo, with Strings (as byte[]) (100grids)
  - rust  : 8.498 (1x, 8.498><8.498)

./sudoku_specialized.mojo : the simple algo, with specialized types (100grids)
  - mojo  : 0.738 (1x, 0.738><0.738)

./sudoku_specialized.rs : the simple algo, with specialized types (100grids)
  - rust  : 0.593 (1x, 0.593><0.593)

./sudoku_specialized_parallel.mojo : the simple algo, with specialized types & parallelization (100grids)
  - mojo  : 0.376 (1x, 0.376><0.376)

optimized/sudoku.java : the optimized algo, with strings (1956grids)
  - java  : 92.164 (1x, 92.164><92.164)

optimized/sudoku.mojo : the optimized algo, with strings (1956grids)
  - mojo  : 55.584 (1x, 55.584><55.584)

optimized/sudoku.py : the optimized algo, with strings (1956grids)
  - codon : 74.405 (1x, 74.405><74.405)
  - py3   : 151.261 (1x, 151.261><151.261)
  - pypy  : 88.126 (1x, 88.126><88.126)

optimized/sudoku_specialized.mojo : optimized algo, with specialized types (1956grids)
  - mojo  : 1.734 (1x, 1.734><1.734)

optimized/sudoku_specialized.rs : the optimized algo, with ultra-specialized types/api (1956grids)
  - rust  : 2.576 (1x, 2.576><2.576)

optimized/sudoku_specialized2.rs : the optimized algo, with specialized types (and readable) (1956grids)
  - rust  : 5.780 (1x, 5.780><5.780)

optimized/sudoku_specialized_parallel.mojo : optimized algo, with specialized types & parallelization (1956grids)
  - mojo  : 0.876 (1x, 0.876><0.876)

```
