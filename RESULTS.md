# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.go : algo with strings
  - go    : 15.224 seconds (87x, 14.506><16.178)

sudoku.java : algo with strings
  - java  : 22.396 seconds (24x, 22.124><22.792)

sudoku.js : algo with strings
  - node  : 31.143 seconds (3x, 30.357><31.192)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 49.294 seconds (30x, 48.860><49.805)

sudoku.nim : algo with strings
  - nim   : 21.290 seconds (66x, 20.252><22.670)

sudoku.py : algo with strings
  - codon : 12.173 seconds (104x, 11.579><12.610)
  - py3   : 104.802 seconds (104x, 100.134><107.987)
  - pypy  : 19.923 seconds (35x, 18.433><20.638)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 8.471 seconds (12x, 8.459><8.748)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.mojo : algo with specialized types (use python to read stdin)
  - mojo  : 1.742 seconds (30x, 1.723><1.776)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.905 seconds (12x, 0.898><0.913)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.2.0-1019-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.85 bogomips)
MEMINFO  : 16365024 kB

codon : 0.16.3
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.18.1 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 11.0.22 2024-01-16
        /usr/bin/javac <file> && /usr/bin/java Sudoku < grids.txt
mojo  : mojo 0.7.0 (af002202)
        /home/runner/.modular/pkg/packages.modular.com_mojo/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.2 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger <file> && ./sudoku < grids.txt
node  : v18.19.1
        /usr/local/bin/node <file> < grids.txt
py3   : Python 3.10.12
        /usr/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.18 (9c4f8ef178b6, Jan 14 2024, 11:28:13)
        /opt/hostedtoolcache/PyPy/3.9.18/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.76.0 (07dca489a 2024-02-04)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


