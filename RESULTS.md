# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.go : algo with strings
  - go    : 15.230 seconds (41x, 15.130><16.178)

sudoku.java : algo with strings
  - java  : 22.446 seconds (60x, 21.454><23.575)

sudoku.js : algo with strings
  - node  : 30.443 seconds (31x, 29.672><32.098)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 49.440 seconds (20x, 49.156><51.143)

sudoku.nim : algo with strings
  - nim   : 21.288 seconds (20x, 21.160><22.358)

sudoku.py : algo with strings
  - codon : 12.156 seconds (58x, 12.067><12.610)
  - py3   : 104.362 seconds (58x, 101.887><107.829)
  - pypy  : 19.643 seconds (58x, 19.095><20.650)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 8.731 seconds (24x, 8.662><9.072)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.mojo : algo with specialized types (use python to read stdin)
  - mojo  : 1.746 seconds (18x, 1.726><1.812)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.620 seconds (24x, 0.615><0.630)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.2.0-1018-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.86 bogomips)
MEMINFO  : 16365028 kB

codon : 0.16.3
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.18.1 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 11.0.21 2023-10-17
        /usr/bin/javac <file> && /usr/bin/java Sudoku < grids.txt
mojo  : mojo 0.6.1 (876ded2e)
        /home/runner/.modular/pkg/packages.modular.com_mojo/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.2 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger <file> && ./sudoku < grids.txt
node  : v18.19.0
        /usr/local/bin/node <file> < grids.txt
py3   : Python 3.10.12
        /usr/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.18 (c5262994620471e725f57d652d78d842270649d6, Sep 27 2023, 13:43:44)
        /opt/hostedtoolcache/PyPy/3.9.18/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.74.1 (a28077b28 2023-12-04)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


