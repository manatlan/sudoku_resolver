# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.go : algo with strings
  - go    : 15.219 seconds (171x, 14.506><16.690)

sudoku.java : algo with strings
  - java  : 22.605 seconds (2x, 22.566><22.644)

sudoku.js : algo with strings
  - node  : 29.757 seconds (30x, 29.078><32.116)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 78.571 seconds (15x, 78.396><79.446)

sudoku.nim : algo with strings
  - nim   : 21.323 seconds (31x, 21.083><22.407)

sudoku.py : algo with strings
  - codon : 12.184 seconds (188x, 11.579><13.244)
  - py3   : 105.174 seconds (188x, 100.134><113.932)
  - pypy  : 18.932 seconds (2x, 18.863><19.001)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 8.680 seconds (2x, 8.601><8.759)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.mojo : algo with specialized types (use python to read stdin)
  - mojo  : 2.235 seconds (15x, 2.208><2.291)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.897 seconds (2x, 0.892><0.902)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.5.0-1021-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.84 bogomips)
MEMINFO  : 16364604 kB

codon : 0.16.3
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.18.1 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 11.0.23 2024-04-16
        /usr/bin/javac <file> && /usr/bin/java Sudoku < grids.txt
mojo  : mojo 24.3.0 (9882e19d)
        /home/runner/.modular/pkg/packages.modular.com_mojo/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.4 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger <file> && ./sudoku < grids.txt
node  : v18.20.2
        /usr/local/bin/node <file> < grids.txt
py3   : Python 3.10.12
        /usr/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.78.0 (9b00956e5 2024-04-29)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


