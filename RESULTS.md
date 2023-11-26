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
  - gcc   : 2.832 (3x, 2.578><2.924)

./sudoku.java : the simple algo, with strings (100grids)
  - java  : 18.961 (3x, 17.464><20.707)

./sudoku.js : the simple algo, with strings (AI translation from java one) (100grids)
  - node  : 34.160 (3x, 31.657><34.195)

./sudoku.mojo : the simple algo, with strings (100grids)
  - mojo  : 15.850 (3x, 15.046><16.032)

./sudoku.nim : the simple algo, with strings (100grids)
  - nim   : 9.114 (3x, 8.324><9.156)

./sudoku.py : the simple algo, with strings (100grids)
  - codon : 15.901 (3x, 15.153><15.924)
  - py3   : 31.469 (3x, 28.524><36.911)
  - pypy  : 14.208 (3x, 13.327><14.484)

./sudoku.rs : the simple algo, with Strings (as byte[]) (100grids)
  - rust  : 8.498 (3x, 6.204><9.479)

./sudoku_specialized.mojo : the simple algo, with specialized types (100grids)
  - mojo  : 0.738 (3x, 0.688><0.747)

./sudoku_specialized.rs : the simple algo, with specialized types (100grids)
  - rust  : 0.585 (3x, 0.543><0.593)

./sudoku_specialized_parallel.mojo : the simple algo, with specialized types & parallelization (100grids)
  - mojo  : 0.376 (3x, 0.365><0.379)

optimized/sudoku.java : the optimized algo, with strings (1956grids)
  - java  : 92.164 (3x, 86.536><101.923)

optimized/sudoku.mojo : the optimized algo, with strings (1956grids)
  - mojo  : 55.584 (3x, 51.318><56.144)

optimized/sudoku.py : the optimized algo, with strings (1956grids)
  - codon : 74.319 (3x, 69.781><74.405)
  - py3   : 151.261 (3x, 129.234><171.793)
  - pypy  : 85.331 (3x, 78.142><88.126)

optimized/sudoku_specialized.mojo : optimized algo, with specialized types (1956grids)
  - mojo  : 1.726 (3x, 1.618><1.734)

optimized/sudoku_specialized.rs : the optimized algo, with ultra-specialized types/api (1956grids)
  - rust  : 2.574 (3x, 2.416><2.576)

optimized/sudoku_specialized2.rs : the optimized algo, with specialized types (and readable) (1956grids)
  - rust  : 5.719 (3x, 5.387><5.780)

optimized/sudoku_specialized_parallel.mojo : optimized algo, with specialized types & parallelization (1956grids)
  - mojo  : 0.876 (3x, 0.854><0.902)

```
