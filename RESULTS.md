# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.go : algo with strings
  - go    : 15.224 seconds (284x, 14.506><16.847)

sudoku.java : algo with strings
  - java  : 22.372 seconds (38x, 22.072><23.730)

sudoku.js : algo with strings
  - node  : 29.302 seconds (52x, 28.966><31.392)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 80.714 seconds (93x, 78.375><86.289)

sudoku.nim : algo with strings
  - nim   : 20.877 seconds (66x, 20.593><22.520)

sudoku.py : algo with strings
  - codon : 12.348 seconds (18x, 12.272><12.589)
  - py3   : 104.959 seconds (301x, 100.134><113.932)
  - pypy  : 19.054 seconds (115x, 18.240><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 12.536 seconds (26x, 12.412><12.726)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.796 seconds (26x, 0.788><0.805)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.5.0-1025-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.86 bogomips)
MEMINFO  : 16364592 kB

codon : 0.17.0
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.18.1 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 11.0.24 2024-07-16
        /usr/bin/javac <file> && /usr/bin/java Sudoku < grids.txt
mojo  : mojo 24.4.0 (2cb57382)
        /home/runner/.modular/pkg/packages.modular.com_mojo/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.8 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger <file> && ./sudoku < grids.txt
node  : v18.20.4
        /usr/local/bin/node <file> < grids.txt
py3   : Python 3.10.12
        /usr/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.80.1 (3f5fd8dd4 2024-08-06)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


