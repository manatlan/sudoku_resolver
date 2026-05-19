# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.c : algo with strings (made by gemini3 from py version)
  - c     : 1.960 seconds (82x, 1.616><2.174)

sudoku.go : algo with strings
  - go    : 16.663 seconds (307x, 11.005><17.145)

sudoku.java : algo with strings
  - java  : 27.029 seconds (5x, 26.685><27.640)

sudoku.js : algo with strings
  - node  : 30.050 seconds (46x, 22.381><33.246)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 22.643 seconds (148x, 16.279><24.433)

sudoku.nim : algo with strings
  - nim   : 23.283 seconds (155x, 18.842><24.795)

sudoku.php : algo with strings
  - php   : 80.229 seconds (4x, 79.641><84.928)

sudoku.py : algo with strings
  - codon : 13.592 seconds (76x, 10.733><14.098)
  - py3   : 88.107 seconds (307x, 69.709><99.134)
  - pypy  : 18.872 seconds (539x, 13.837><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 4.451 seconds (5x, 4.271><4.547)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.c : algo OPTIMIZED (by copilot)
  - c     : 0.130 seconds (82x, 0.114><0.147)

specialized/sudoku.go : algo with arrays (optimized by copilot)
  - go    : 2.234 seconds (157x, 1.871><2.427)

specialized/sudoku.nim : algo with specialized types using bitsets (optimized by copilot)
  - nim   : 1.093 seconds (155x, 0.885><1.287)

specialized/sudoku.py : algo with specialized types/logics (optimized by copilot)
  - codon : 0.821 seconds (76x, 0.634><0.881)
  - py3   : 16.569 seconds (155x, 12.993><17.648)
  - pypy  : 1.095 seconds (155x, 0.838><1.250)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.743 seconds (5x, 0.671><0.754)

specialized/sudoku2.go : from c to go (by gemini3)
  - go    : 0.377 seconds (150x, 0.294><0.435)

specialized/sudoku2.nim : from c to nim (by gemini3)
  - nim   : 0.226 seconds (150x, 0.193><0.260)

specialized/sudoku2.py : conversion from C to py3 (by gemini3)
  - codon : 1.041 seconds (76x, 0.832><1.085)
  - py3   : 11.983 seconds (151x, 9.003><13.681)
  - pypy  : 2.800 seconds (151x, 2.290><3.517)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.17.0-1013-azure-x86_64-with-glibc2.39 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.86 bogomips)
MEMINFO  : 16373460 kB

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
node  : v20.20.2
        /usr/local/bin/node <file> < grids.txt
php   : PHP 8.3.31 (cli) (built: May 15 2026 00:11:57) (NTS)
        /usr/bin/php <file> < grids.txt
py3   : Python 3.12.3
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.95.0 (59807616e 2026-04-14)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


