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
  - gcc   : 2.854 (4x, 2.768><2.898)

./sudoku.java : the simple algo, with strings (100grids)
  - java  : 20.154 (4x, 19.230><23.276)

./sudoku.js : the simple algo, with strings (AI translation from java one) (100grids)
  - node  : 34.736 (4x, 34.237><34.927)

./sudoku.mojo : the simple algo, with strings (100grids)
  - mojo  : 15.895 (4x, 15.877><15.991)

./sudoku.nim : the simple algo, with strings (100grids)
  - nim   : 9.038 (4x, 8.990><9.170)

./sudoku.py : the simple algo, with strings (100grids)
  - codon : 16.038 (4x, 15.931><16.068)
  - py3   : 35.456 (4x, 29.781><44.082)
  - pypy  : 14.143 (4x, 13.628><14.329)

./sudoku.rs : the simple algo, with Strings (as byte[]) (100grids)
  - rust  : 8.191 (4x, 7.289><10.177)

./sudoku_specialized.mojo : the simple algo, with specialized types (100grids)
  - mojo  : 0.738 (4x, 0.735><0.739)

./sudoku_specialized.rs : the simple algo, with specialized types (100grids)
  - rust  : 0.585 (4x, 0.584><0.590)

./sudoku_specialized_parallel.mojo : the simple algo, with specialized types & parallelization (100grids)
  - mojo  : 0.377 (4x, 0.376><0.396)

optimized/sudoku.java : the optimized algo, with strings (1956grids)
  - java  : 100.716 (4x, 91.851><103.893)

optimized/sudoku.mojo : the optimized algo, with strings (1956grids)
  - mojo  : 55.343 (4x, 55.175><55.721)

optimized/sudoku.py : the optimized algo, with strings (1956grids)
  - codon : 74.418 (4x, 74.247><75.214)
  - py3   : 143.925 (4x, 135.572><147.016)
  - pypy  : 86.976 (4x, 86.127><93.074)

optimized/sudoku_specialized.mojo : optimized algo, with specialized types (1956grids)
  - mojo  : 1.747 (4x, 1.735><1.753)

optimized/sudoku_specialized.rs : the optimized algo, with specialized types (and readable) (1956grids)
  - rust  : 0.643 (4x, 0.643><0.652)

optimized/sudoku_specialized_parallel.mojo : optimized algo, with specialized types & parallelization (1956grids)
  - mojo  : 0.883 (4x, 0.876><0.883)

```
