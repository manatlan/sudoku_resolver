
# Result on fv-az569-968

```
PLATFORM : x86_64/Linux-6.2.0-1016-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.84 bogomips)
MEMINFO  : 16365020 kB

java  : openjdk 11.0.21 2023-10-17
        /usr/bin/java <file>
node  : v18.18.2
        /usr/local/bin/node <file>
py3   : Python 3.10.12
        /usr/bin/python3 -uOO <file>
rust  : rustc 1.73.0 (cc66ad468 2023-10-03)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o exe && ./exe
gcc   : gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
        /usr/bin/gcc <file> -o exe && ./exe

```

## Simple Algo

For the first 100 grids : At each iteration, they will resolve the first hole of the grid, til no holes.
(*specialized* versions use all weapons available in language, while others use string and hashset)
```

sudoku.rs : the simple algo, with Strings (as byte[]) (100grids)
  - rust  : 18.977 seconds (1x, 18.977><18.977)

sudoku_specialized.rs : the simple algo, with specialized types (100grids)
  - rust  : 1.315 seconds (1x, 1.315><1.315)

```

## Optimized Algo

For **all 1956** grids : At each iteration, they will firstly resolve the hole, with minimal choices, of the grid, til no holes.
(*specialized* versions use all weapons available in language, while others use string and hashset)

```

optimized/sudoku_specialized.rs : the optimized algo, with specialized types (and readable) (1956grids)
  - rust  : 1.248 seconds (1x, 1.248><1.248)

```


