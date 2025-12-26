# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.c : algo with strings (made by gemini3 from py version)
  - c     : 1.951 seconds (11x, 1.947><2.173)

sudoku.go : algo with strings
  - go    : 16.668 seconds (165x, 15.152><17.145)

sudoku.java : algo with strings
  - java  : 27.015 seconds (12x, 21.194><28.987)

sudoku.js : algo with strings
  - node  : 30.301 seconds (22x, 27.547><31.214)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 22.642 seconds (22x, 22.046><23.538)

sudoku.nim : algo with strings
  - nim   : 23.107 seconds (13x, 22.735><23.823)

sudoku.php : algo with strings
  - php   : 82.144 seconds (22x, 69.074><82.950)

sudoku.py : algo with strings
  - codon : 13.812 seconds (22x, 12.617><14.882)
  - py3   : 88.455 seconds (165x, 86.241><93.138)
  - pypy  : 19.010 seconds (397x, 17.905><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 6.247 seconds (17x, 6.034><6.287)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.c : algo OPTIMIZED (by copilot)
  - c     : 0.130 seconds (10x, 0.129><0.141)

specialized/sudoku.go : algo with arrays (optimized by copilot)
  - go    : 2.233 seconds (15x, 2.222><2.375)

specialized/sudoku.nim : algo with specialized types using bitsets (optimized by copilot)
  - nim   : 1.089 seconds (13x, 1.039><1.095)

specialized/sudoku.py : algo with specialized types/logics (optimized by copilot)
  - codon : 0.816 seconds (13x, 0.808><0.866)
  - py3   : 16.181 seconds (13x, 14.720><16.419)
  - pypy  : 1.094 seconds (13x, 1.079><1.167)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.686 seconds (17x, 0.677><0.713)

specialized/sudoku2.go : from c to go (by gemini3)
  - go    : 0.375 seconds (8x, 0.366><0.426)

specialized/sudoku2.nim : from c to nim (by gemini3)
  - nim   : 0.225 seconds (8x, 0.219><0.245)

specialized/sudoku2.py : conversion from C to py3 (by gemini3)
  - codon : 1.049 seconds (9x, 1.031><1.109)
  - py3   : 11.983 seconds (9x, 11.164><12.342)
  - pypy  : 2.787 seconds (9x, 2.763><3.517)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.11.0-1018-azure-x86_64-with-glibc2.39 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.85 bogomips)
MEMINFO  : 16379468 kB

c     : gcc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0
        /usr/bin/gcc -O3 <file> -o ./sudoku && ./sudoku < grids.txt
codon : 0.19.4
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.22.2 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 17.0.17 2025-10-21
        /usr/bin/javac -d . <file> && /usr/bin/java Sudoku < grids.txt
mojo  : Mojo 0.25.7.0 (e5af2b2f)
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.16 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger -o:sudoku <file> && ./sudoku < grids.txt
node  : v20.19.6
        /usr/local/bin/node <file> < grids.txt
php   : PHP 8.3.28 (cli) (built: Dec  9 2025 12:37:08) (NTS)
        /usr/bin/php <file> < grids.txt
py3   : Python 3.12.3
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.92.0 (ded5c06cf 2025-12-08)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


