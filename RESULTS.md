# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Results

All implementations use same bases types (string)

```

sudoku.go : algo with strings
  - go    : 15.230 seconds (3x, 15.180><15.296)

sudoku.java : algo with strings
  - java  : 22.417 seconds (22x, 22.136><22.790)

sudoku.js : algo with strings
  - node  : 29.733 seconds (22x, 29.531><31.323)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 82.479 seconds (9x, 81.830><84.673)

sudoku.nim : algo with strings
  - nim   : 23.796 seconds (22x, 23.325><25.014)

sudoku.py : algo with strings
  - codon : 12.185 seconds (20x, 12.094><12.353)
  - py3   : 103.641 seconds (20x, 101.887><107.829)
  - pypy  : 19.604 seconds (20x, 19.177><20.424)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 8.725 seconds (14x, 8.692><8.881)

```

## SPECIALIZED Results

It's the same algorithm, but use weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.mojo : algo with specialized types (use python to read stdin)
  - mojo  : 1.741 seconds (9x, 1.717><1.748)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.623 seconds (22x, 0.616><0.627)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.2.0-1016-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.85 bogomips)
MEMINFO  : 16365020 kB

codon : 0.16.3
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.18.1 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 11.0.21 2023-10-17
        /usr/bin/javac <file> && /usr/bin/java Sudoku < grids.txt
mojo  : mojo 0.5.1 (6e50a738)
        /home/runner/.modular/pkg/packages.modular.com_mojo/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.0 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger <file> && ./sudoku < grids.txt
node  : v18.18.2
        /usr/local/bin/node <file> < grids.txt
py3   : Python 3.10.12
        /usr/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.18 (c5262994620471e725f57d652d78d842270649d6, Sep 27 2023, 13:43:44)
        /opt/hostedtoolcache/PyPy/3.9.18/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.74.0 (79e9716c9 2023-11-13)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


