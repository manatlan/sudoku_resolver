# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.go : algo with strings
  - go    : 15.238 seconds (372x, 14.506><16.847)

sudoku.java : algo with strings
  - java  : 22.424 seconds (32x, 21.218><23.108)

sudoku.js : algo with strings
  - node  : 29.475 seconds (22x, 28.999><33.129)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 80.768 seconds (181x, 78.375><86.289)

sudoku.nim : algo with strings
  - nim   : 22.692 seconds (36x, 22.301><23.675)

sudoku.py : algo with strings
  - codon : 12.357 seconds (106x, 12.270><12.589)
  - py3   : 104.796 seconds (389x, 100.134><113.932)
  - pypy  : 19.091 seconds (203x, 18.240><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 12.903 seconds (9x, 12.787><13.024)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.637 seconds (9x, 0.634><0.645)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.5.0-1025-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.85 bogomips)
MEMINFO  : 16364592 kB

codon : 0.17.0
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.18.1 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 11.0.25 2024-10-15
        /usr/bin/javac <file> && /usr/bin/java Sudoku < grids.txt
mojo  : mojo 24.4.0 (2cb57382)
        /home/runner/.modular/pkg/packages.modular.com_mojo/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.12 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger <file> && ./sudoku < grids.txt
node  : v18.20.5
        /usr/local/bin/node <file> < grids.txt
py3   : Python 3.10.12
        /usr/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.83.0 (90b35a623 2024-11-26)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


