# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.c : algo with strings (made by gemini3 from py version)
  - c     : 1.958 seconds (73x, 1.616><2.174)

sudoku.go : algo with strings
  - go    : 16.664 seconds (298x, 11.005><17.145)

sudoku.java : algo with strings
  - java  : 27.139 seconds (99x, 19.228><30.332)

sudoku.js : algo with strings
  - node  : 30.049 seconds (37x, 22.381><33.246)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 22.644 seconds (143x, 16.279><24.433)

sudoku.nim : algo with strings
  - nim   : 23.259 seconds (146x, 18.842><24.795)

sudoku.php : algo with strings
  - php   : 71.430 seconds (2x, 61.382><81.478)

sudoku.py : algo with strings
  - codon : 13.573 seconds (67x, 10.733><14.098)
  - py3   : 88.106 seconds (298x, 69.709><93.138)
  - pypy  : 18.892 seconds (530x, 13.837><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 4.332 seconds (17x, 3.442><4.502)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.c : algo OPTIMIZED (by copilot)
  - c     : 0.130 seconds (73x, 0.114><0.147)

specialized/sudoku.go : algo with arrays (optimized by copilot)
  - go    : 2.234 seconds (148x, 1.871><2.427)

specialized/sudoku.nim : algo with specialized types using bitsets (optimized by copilot)
  - nim   : 1.093 seconds (146x, 0.885><1.287)

specialized/sudoku.py : algo with specialized types/logics (optimized by copilot)
  - codon : 0.821 seconds (67x, 0.634><0.881)
  - py3   : 16.575 seconds (146x, 12.993><17.648)
  - pypy  : 1.093 seconds (146x, 0.838><1.167)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.704 seconds (17x, 0.584><0.745)

specialized/sudoku2.go : from c to go (by gemini3)
  - go    : 0.377 seconds (141x, 0.294><0.435)

specialized/sudoku2.nim : from c to nim (by gemini3)
  - nim   : 0.226 seconds (141x, 0.193><0.260)

specialized/sudoku2.py : conversion from C to py3 (by gemini3)
  - codon : 1.042 seconds (67x, 0.832><1.085)
  - py3   : 11.984 seconds (142x, 9.003><13.681)
  - pypy  : 2.798 seconds (142x, 2.290><3.517)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.17.0-1010-azure-x86_64-with-glibc2.39 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.86 bogomips)
MEMINFO  : 16373460 kB

c     : gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
        /usr/bin/gcc -O3 <file> -o ./sudoku && ./sudoku < grids.txt
codon : 0.19.6
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.22.2 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 17.0.18 2026-01-20
        /usr/bin/javac -d . <file> && /usr/bin/java Sudoku < grids.txt
mojo  : Mojo 0.25.7.0 (e5af2b2f)
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.16 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger -o:sudoku <file> && ./sudoku < grids.txt
node  : v20.20.2
        /usr/local/bin/node <file> < grids.txt
php   : PHP 8.3.31 (cli) (built: May  8 2026 04:45:26) (NTS)
        /usr/bin/php <file> < grids.txt
py3   : Python 3.12.3
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.94.1 (e408947bf 2026-03-25)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


