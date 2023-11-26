# Host infos
```
PLATFORM : x86_64/Linux-6.2.0-1016-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.86 bogomips)
MEMINFO  : 16365016 kB
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
  - gcc   : 2.705 (2x, 2.578><2.832)

./sudoku.java : the simple algo, with strings (100grids)
  - java  : 19.085 (2x, 17.464><20.707)

./sudoku.js : the simple algo, with strings (AI translation from java one) (100grids)
  - node  : 32.908 (2x, 31.657><34.160)

./sudoku.mojo : the simple algo, with strings (100grids)
  - mojo  : 15.539 (2x, 15.046><16.032)

./sudoku.nim : the simple algo, with strings (100grids)
  - nim   : 8.719 (2x, 8.324><9.114)

./sudoku.py : the simple algo, with strings (100grids)
  - codon : 15.538 (2x, 15.153><15.924)
  - py3   : 32.718 (2x, 28.524><36.911)
  - pypy  : 13.905 (2x, 13.327><14.484)

./sudoku.rs : the simple algo, with Strings (as byte[]) (100grids)
  - rust  : 8.988 (2x, 8.498><9.479)

./sudoku_specialized.mojo : the simple algo, with specialized types (100grids)
  - mojo  : 0.713 (2x, 0.688><0.738)

./sudoku_specialized.rs : the simple algo, with specialized types (100grids)
  - rust  : 0.568 (2x, 0.543><0.593)

./sudoku_specialized_parallel.mojo : the simple algo, with specialized types & parallelization (100grids)
  - mojo  : 0.370 (2x, 0.365><0.376)

optimized/sudoku.java : the optimized algo, with strings (1956grids)
  - java  : 89.350 (2x, 86.536><92.164)

optimized/sudoku.mojo : the optimized algo, with strings (1956grids)
  - mojo  : 53.451 (2x, 51.318><55.584)

optimized/sudoku.py : the optimized algo, with strings (1956grids)
  - codon : 72.093 (2x, 69.781><74.405)
  - py3   : 140.248 (2x, 129.234><151.261)
  - pypy  : 83.134 (2x, 78.142><88.126)

optimized/sudoku_specialized.mojo : optimized algo, with specialized types (1956grids)
  - mojo  : 1.676 (2x, 1.618><1.734)

optimized/sudoku_specialized.rs : the optimized algo, with ultra-specialized types/api (1956grids)
  - rust  : 2.496 (2x, 2.416><2.576)

optimized/sudoku_specialized2.rs : the optimized algo, with specialized types (and readable) (1956grids)
  - rust  : 5.583 (2x, 5.387><5.780)

optimized/sudoku_specialized_parallel.mojo : optimized algo, with specialized types & parallelization (1956grids)
  - mojo  : 0.865 (2x, 0.854><0.876)

```
