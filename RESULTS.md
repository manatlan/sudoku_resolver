# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.c : algo with strings (made by gemini3 from py version)
  - c     : 1.963 seconds (101x, 1.616><2.174)

sudoku.go : algo with strings
  - go    : 16.660 seconds (326x, 10.990><17.145)

sudoku.java : algo with strings
  - java  : 27.078 seconds (24x, 19.218><29.053)

sudoku.js : algo with strings
  - node  : 27.555 seconds (16x, 26.688><29.313)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 22.639 seconds (155x, 16.168><24.433)

sudoku.nim : algo with strings
  - nim   : 23.306 seconds (174x, 18.631><24.795)

sudoku.php : algo with strings
  - php   : 80.465 seconds (23x, 63.145><85.118)

sudoku.py : algo with strings
  - codon : 13.600 seconds (95x, 10.701><14.098)
  - py3   : 88.094 seconds (326x, 67.401><99.134)
  - pypy  : 18.854 seconds (558x, 13.837><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 4.429 seconds (24x, 3.449><4.547)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.c : algo OPTIMIZED (by copilot)
  - c     : 0.130 seconds (101x, 0.114><0.148)

specialized/sudoku.go : algo with arrays (optimized by copilot)
  - go    : 2.235 seconds (176x, 1.867><2.433)

specialized/sudoku.nim : algo with specialized types using bitsets (optimized by copilot)
  - nim   : 1.094 seconds (174x, 0.885><1.287)

specialized/sudoku.py : algo with specialized types/logics (optimized by copilot)
  - codon : 0.819 seconds (95x, 0.633><0.881)
  - py3   : 16.569 seconds (174x, 12.858><17.648)
  - pypy  : 1.097 seconds (174x, 0.834><1.250)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.743 seconds (24x, 0.591><0.756)

specialized/sudoku2.go : from c to go (by gemini3)
  - go    : 0.378 seconds (169x, 0.294><0.435)

specialized/sudoku2.nim : from c to nim (by gemini3)
  - nim   : 0.227 seconds (169x, 0.193><0.274)

specialized/sudoku2.py : conversion from C to py3 (by gemini3)
  - codon : 1.042 seconds (95x, 0.830><1.085)
  - py3   : 11.962 seconds (170x, 8.952><13.681)
  - pypy  : 2.803 seconds (170x, 2.287><3.517)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.17.0-1015-azure-x86_64-with-glibc2.39 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 9V74 80-Core Processor" (5192.26 bogomips)
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
node  : v22.22.3
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


