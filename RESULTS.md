# Host infos
```
PLATFORM : x86_64/Linux-6.2.0-1016-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.85 bogomips)
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
  - gcc   : 2.818 (1x, 2.818><2.818)

./sudoku.java : the simple algo, with strings (100grids)
  - java  : 19.083 (1x, 19.083><19.083)

./sudoku.js : the simple algo, with strings (AI translation from java one) (100grids)
  - node  : 34.493 (1x, 34.493><34.493)

./sudoku.mojo : the simple algo, with strings (100grids)
  - mojo  : 15.933 (1x, 15.933><15.933)

./sudoku.nim : the simple algo, with strings (100grids)
  - nim   : 9.023 (1x, 9.023><9.023)

./sudoku.py : the simple algo, with strings (100grids)
  - codon : 15.930 (1x, 15.930><15.930)
  - py3   : 33.655 (1x, 33.655><33.655)
  - pypy  : 13.967 (1x, 13.967><13.967)

./sudoku.rs : the simple algo, with strings (AI translation from java one) (100grids)
  - rust  : 25.940 (1x, 25.940><25.940)

./sudoku_specialized.mojo : the simple algo, with specialized types (100grids)
  - mojo  : 0.742 (1x, 0.742><0.742)

./sudoku_specialized.rs : the simple algo, with specialized types (100grids)
  - rust  : 0.587 (1x, 0.587><0.587)

./sudoku_specialized_parallel.mojo : the simple algo, with specialized types & parallelization (100grids)
  - mojo  : 0.377 (1x, 0.377><0.377)

optimized/sudoku.java : the optimized algo, with strings (1956grids)
  - java  : 98.194 (1x, 98.194><98.194)

optimized/sudoku.mojo : the optimized algo, with strings (1956grids)
  - mojo  : 55.233 (1x, 55.233><55.233)

optimized/sudoku.py : the optimized algo, with strings (1956grids)
  - codon : 74.896 (1x, 74.896><74.896)
  - py3   : 153.512 (1x, 153.512><153.512)
  - pypy  : 88.545 (1x, 88.545><88.545)

optimized/sudoku_specialized.mojo : optimized algo, with specialized types (1956grids)
  - mojo  : 1.732 (1x, 1.732><1.732)

optimized/sudoku_specialized.rs : the optimized algo, with ultra-specialized types/api (1956grids)
  - rust  : 2.593 (1x, 2.593><2.593)

optimized/sudoku_specialized_parallel.mojo : optimized algo, with specialized types & parallelization (1956grids)
  - mojo  : 0.876 (1x, 0.876><0.876)

```
