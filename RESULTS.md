# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.c : algo with strings (made by gemini3 from py version)
  - c     : 1.961 seconds (130x, 1.377><2.174)

sudoku.go : algo with strings
  - go    : 16.661 seconds (355x, 9.018><17.145)

sudoku.java : algo with strings
  - java  : 27.084 seconds (53x, 13.164><29.328)

sudoku.js : algo with strings
  - node  : 28.028 seconds (6x, 26.356><30.103)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 22.615 seconds (178x, 12.584><24.433)

sudoku.nim : algo with strings
  - nim   : 23.321 seconds (203x, 12.758><24.795)

sudoku.php : algo with strings
  - php   : 75.917 seconds (4x, 68.603><83.048)

sudoku.py : algo with strings
  - codon : 13.604 seconds (124x, 7.802><14.098)
  - py3   : 88.058 seconds (355x, 45.878><99.134)
  - pypy  : 18.837 seconds (587x, 10.538><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 4.295 seconds (26x, 2.871><4.495)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.c : algo OPTIMIZED (by copilot)
  - c     : 0.130 seconds (130x, 0.105><0.148)

specialized/sudoku.go : algo with arrays (optimized by copilot)
  - go    : 2.236 seconds (205x, 1.490><2.433)

specialized/sudoku.nim : algo with specialized types using bitsets (optimized by copilot)
  - nim   : 1.094 seconds (203x, 0.694><1.287)

specialized/sudoku.py : algo with specialized types/logics (optimized by copilot)
  - codon : 0.820 seconds (124x, 0.500><0.887)
  - py3   : 16.567 seconds (203x, 8.973><17.875)
  - pypy  : 1.099 seconds (203x, 0.572><1.260)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.681 seconds (26x, 0.429><0.766)

specialized/sudoku2.go : from c to go (by gemini3)
  - go    : 0.378 seconds (198x, 0.256><0.436)

specialized/sudoku2.nim : from c to nim (by gemini3)
  - nim   : 0.227 seconds (198x, 0.175><0.274)

specialized/sudoku2.py : conversion from C to py3 (by gemini3)
  - codon : 1.043 seconds (124x, 0.690><1.085)
  - py3   : 11.958 seconds (199x, 6.591><13.681)
  - pypy  : 2.804 seconds (199x, 1.720><3.517)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.17.0-1018-azure-x86_64-with-glibc2.39 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.85 bogomips)
MEMINFO  : 16377692 kB

c     : gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
        /usr/bin/gcc -O3 <file> -o ./sudoku && ./sudoku < grids.txt
codon : 0.19.6
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.22.2 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 17.0.19 2026-04-21
        /usr/bin/javac -d . <file> && /usr/bin/java Sudoku < grids.txt
mojo  : Mojo 0.25.7.0 (e5af2b2f)
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.16 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger -o:sudoku <file> && ./sudoku < grids.txt
node  : v22.23.1
        /usr/local/bin/node <file> < grids.txt
php   : PHP 8.3.32 (cli) (built: Jul  4 2026 14:25:46) (NTS)
        /usr/bin/php <file> < grids.txt
py3   : Python 3.12.3
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.96.0 (ac68faa20 2026-05-25)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


