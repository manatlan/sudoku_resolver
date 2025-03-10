# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.go : algo with strings
  - go    : 16.669 seconds (56x, 16.588><16.955)

sudoku.java : algo with strings
  - java  : 27.065 seconds (38x, 26.595><29.315)

sudoku.js : algo with strings
  - node  : 30.294 seconds (12x, 30.051><30.899)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 80.739 seconds (210x, 78.375><86.289)

sudoku.nim : algo with strings
  - nim   : 23.302 seconds (74x, 22.279><24.479)

sudoku.py : algo with strings
  - codon : 13.529 seconds (26x, 13.420><13.835)
  - py3   : 88.755 seconds (56x, 86.923><93.035)
  - pypy  : 19.069 seconds (288x, 18.240><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 7.992 seconds (12x, 7.957><8.035)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.651 seconds (12x, 0.646><0.667)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.8.0-1021-azure-x86_64-with-glibc2.39 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.85 bogomips)
MEMINFO  : 16373792 kB

codon : 0.18.1
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.22.2 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 17.0.14 2025-01-21
        /usr/bin/javac <file> && /usr/bin/java Sudoku < grids.txt
mojo  : mojo 24.4.0 (2cb57382)
        /home/runner/.modular/pkg/packages.modular.com_mojo/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.14 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger <file> && ./sudoku < grids.txt
node  : v20.18.3
        /usr/local/bin/node <file> < grids.txt
py3   : Python 3.12.3
        /usr/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.85.0 (4d91de4e4 2025-02-17)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


