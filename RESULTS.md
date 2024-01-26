# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.go : algo with strings
  - go    : 15.224 seconds (58x, 14.506><16.178)

sudoku.java : algo with strings
  - java  : 22.432 seconds (77x, 21.454><23.575)

sudoku.js : algo with strings
  - node  : 30.431 seconds (48x, 28.896><32.098)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 49.475 seconds (1x, 49.475><49.475)

sudoku.nim : algo with strings
  - nim   : 21.286 seconds (37x, 20.252><22.670)

sudoku.py : algo with strings
  - codon : 12.152 seconds (75x, 11.579><12.610)
  - py3   : 104.689 seconds (75x, 100.134><107.829)
  - pypy  : 20.009 seconds (6x, 18.433><20.530)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 8.682 seconds (13x, 8.224><8.928)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.mojo : algo with specialized types (use python to read stdin)
  - mojo  : 1.746 seconds (1x, 1.746><1.746)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.909 seconds (13x, 0.899><0.934)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.2.0-1018-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.85 bogomips)
MEMINFO  : 16365028 kB

codon : 0.16.3
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.18.1 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 11.0.21 2023-10-17
        /usr/bin/javac <file> && /usr/bin/java Sudoku < grids.txt
mojo  : mojo 0.7.0 (af002202)
        /home/runner/.modular/pkg/packages.modular.com_mojo/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.2 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger <file> && ./sudoku < grids.txt
node  : v18.19.0
        /usr/local/bin/node <file> < grids.txt
py3   : Python 3.10.12
        /usr/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.18 (9c4f8ef178b6, Jan 14 2024, 11:28:13)
        /opt/hostedtoolcache/PyPy/3.9.18/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.75.0 (82e1608df 2023-12-21)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


