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
  - gcc   : 2.871 (3x, 2.837><2.898)

./sudoku.java : the simple algo, with strings (100grids)
  - java  : 19.871 (3x, 19.230><23.276)

./sudoku.js : the simple algo, with strings (AI translation from java one) (100grids)
  - node  : 34.907 (3x, 34.564><34.927)

./sudoku.mojo : the simple algo, with strings (100grids)
  - mojo  : 15.893 (3x, 15.877><15.991)

./sudoku.nim : the simple algo, with strings (100grids)
  - nim   : 9.067 (3x, 9.009><9.170)

./sudoku.py : the simple algo, with strings (100grids)
  - codon : 16.060 (3x, 15.931><16.068)
  - py3   : 38.280 (3x, 29.781><44.082)
  - pypy  : 14.102 (3x, 13.628><14.329)

./sudoku.rs : the simple algo, with Strings (as byte[]) (100grids)
  - rust  : 7.752 (3x, 7.289><8.629)

./sudoku_specialized.mojo : the simple algo, with specialized types (100grids)
  - mojo  : 0.738 (3x, 0.738><0.739)

./sudoku_specialized.rs : the simple algo, with specialized types (100grids)
  - rust  : 0.586 (3x, 0.584><0.590)

./sudoku_specialized_parallel.mojo : the simple algo, with specialized types & parallelization (100grids)
  - mojo  : 0.376 (3x, 0.376><0.396)

optimized/sudoku.java : the optimized algo, with strings (1956grids)
  - java  : 100.932 (3x, 100.501><103.893)

optimized/sudoku.mojo : the optimized algo, with strings (1956grids)
  - mojo  : 55.311 (3x, 55.175><55.375)

optimized/sudoku.py : the optimized algo, with strings (1956grids)
  - codon : 74.510 (3x, 74.247><75.214)
  - py3   : 144.455 (3x, 135.572><147.016)
  - pypy  : 87.222 (3x, 86.127><93.074)

optimized/sudoku_specialized.mojo : optimized algo, with specialized types (1956grids)
  - mojo  : 1.746 (3x, 1.735><1.748)

optimized/sudoku_specialized.rs : the optimized algo, with specialized types (and readable) (1956grids)
  - rust  : 0.643 (3x, 0.643><0.643)

optimized/sudoku_specialized_parallel.mojo : optimized algo, with specialized types & parallelization (1956grids)
  - mojo  : 0.882 (3x, 0.876><0.883)

```
