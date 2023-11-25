# Host infos
```
PLATFORM : x86_64/Linux-6.2.0-1016-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.85 bogomips)
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
  - gcc   : 2.873 (2x, 2.818><2.929)

./sudoku.java : the simple algo, with strings (100grids)
  - java  : 19.762 (2x, 19.083><20.442)

./sudoku.js : the simple algo, with strings (AI translation from java one) (100grids)
  - node  : 34.636 (2x, 34.493><34.780)

./sudoku.mojo : the simple algo, with strings (100grids)
  - mojo  : 15.895 (2x, 15.856><15.933)

./sudoku.nim : the simple algo, with strings (100grids)
  - nim   : 9.037 (2x, 9.023><9.051)

./sudoku.py : the simple algo, with strings (100grids)
  - codon : 15.901 (2x, 15.871><15.930)
  - py3   : 34.380 (2x, 33.655><35.106)
  - pypy  : 13.858 (2x, 13.749><13.967)

./sudoku.rs : the simple algo, with strings (AI translation from java one) (100grids)
  - rust  : 26.281 (2x, 25.940><26.622)

./sudoku_specialized.mojo : the simple algo, with specialized types (100grids)
  - mojo  : 0.740 (2x, 0.738><0.742)

./sudoku_specialized.rs : the simple algo, with specialized types (100grids)
  - rust  : 0.586 (2x, 0.585><0.587)

./sudoku_specialized_parallel.mojo : the simple algo, with specialized types & parallelization (100grids)
  - mojo  : 0.377 (2x, 0.377><0.377)

optimized/sudoku.java : the optimized algo, with strings (1956grids)
  - java  : 98.936 (2x, 98.194><99.678)

optimized/sudoku.mojo : the optimized algo, with strings (1956grids)
  - mojo  : 55.521 (2x, 55.233><55.809)

optimized/sudoku.py : the optimized algo, with strings (1956grids)
  - codon : 75.239 (2x, 74.896><75.582)
  - py3   : 146.270 (2x, 139.029><153.512)
  - pypy  : 88.038 (2x, 87.532><88.545)

optimized/sudoku_specialized.mojo : optimized algo, with specialized types (1956grids)
  - mojo  : 1.741 (2x, 1.732><1.750)

optimized/sudoku_specialized.rs : the optimized algo, with ultra-specialized types/api (1956grids)
  - rust  : 2.589 (2x, 2.585><2.593)

optimized/sudoku_specialized_parallel.mojo : optimized algo, with specialized types & parallelization (1956grids)
  - mojo  : 0.876 (2x, 0.876><0.876)

```
