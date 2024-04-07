# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.go : algo with strings
  - go    : 15.219 seconds (131x, 14.506><16.690)

sudoku.java : algo with strings
  - java  : 22.375 seconds (68x, 21.663><23.928)

sudoku.js : algo with strings
  - node  : 29.662 seconds (2x, 29.573><29.750)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 79.401 seconds (10x, 78.118><81.538)

sudoku.nim : algo with strings
  - nim   : 21.259 seconds (110x, 20.252><22.670)

sudoku.py : algo with strings
  - codon : 12.180 seconds (148x, 11.579><13.244)
  - py3   : 104.968 seconds (148x, 100.134><110.318)
  - pypy  : 19.879 seconds (79x, 18.433><20.917)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 8.525 seconds (2x, 8.509><8.541)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.mojo : algo with specialized types (use python to read stdin)
  - mojo  : 1.630 seconds (10x, 1.609><1.704)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.888 seconds (2x, 0.882><0.893)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.5.0-1017-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.86 bogomips)
MEMINFO  : 16364600 kB

codon : 0.16.3
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.18.1 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 11.0.22 2024-01-16
        /usr/bin/javac <file> && /usr/bin/java Sudoku < grids.txt
mojo  : mojo 24.2.0 (c2427bc5)
        /home/runner/.modular/pkg/packages.modular.com_mojo/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.2 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger <file> && ./sudoku < grids.txt
node  : v18.20.0
        /usr/local/bin/node <file> < grids.txt
py3   : Python 3.10.12
        /usr/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.18 (9c4f8ef178b6, Jan 14 2024, 11:28:13)
        /opt/hostedtoolcache/PyPy/3.9.18/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.77.1 (7cf61ebde 2024-03-27)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


