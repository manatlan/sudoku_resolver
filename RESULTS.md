# Host infos
PLATFORM : x86_64/Linux-6.2.0-1016-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.85 bogomips)
MEMINFO  : 16365020 kB

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
  - gcc   : 2.846 (16x, 2.770><3.097)

./sudoku.java : the simple algo, with strings (100grids)
  - java  : 19.159 (16x, 18.437><23.334)

./sudoku.js : the simple algo, with strings (AI translation from java one) (100grids)
  - node  : 34.540 (16x, 34.189><34.918)

./sudoku.mojo : the simple algo, with strings (100grids)
  - mojo  : 15.969 (16x, 15.850><17.150)

./sudoku.nim : the simple algo, with strings (100grids)
  - nim   : 9.047 (16x, 8.956><9.179)

./sudoku.py : the simple algo, with strings (100grids)
  - codon : 15.995 (16x, 15.914><16.183)
  - py3   : 35.239 (16x, 26.696><44.327)
  - pypy  : 14.078 (16x, 13.673><14.639)

./sudoku.rs : the simple algo, with strings (AI translation from java one) (100grids)
  - rust  : 38.951 (16x, 26.979><48.545)

./sudoku_specialized.mojo : the simple algo, with specialized mojo-types (100grids)
  - mojo  : 0.739 (16x, 0.685><0.773)

./sudoku_specialized.rs : the simple algo, with ultra-specialized types/api (100grids)
  - rust  : 0.605 (16x, 0.602><0.658)

./sudoku_specialized_parallel.mojo : the simple algo, with specialized types & parallelization (100grids)
  - mojo  : 0.378 (16x, 0.374><0.409)

optimized/sudoku.java : the optimized algo, with strings (1956grids)
  - java  : 93.278 (13x, 90.974><103.089)

optimized/sudoku.mojo : the optimized algo, with strings (1956grids)
  - mojo  : 55.268 (13x, 54.922><58.112)

optimized/sudoku.py : the optimized algo, with strings (1956grids)
  - codon : 74.607 (13x, 74.191><75.256)
  - py3   : 146.266 (13x, 125.846><183.164)
  - pypy  : 86.368 (13x, 84.024><87.688)

optimized/sudoku_specialized.mojo : optimized algo, with specialized types (1956grids)
  - mojo  : 1.736 (13x, 1.718><1.768)

optimized/sudoku_specialized.rs : the optimized algo, with ultra-specialized types/api (1956grids)
  - rust  : 2.578 (13x, 2.567><2.618)

optimized/sudoku_specialized_parallel.mojo : optimized algo, with specialized types & parallelization (1956grids)
  - mojo  : 0.881 (13x, 0.874><0.901)

```
