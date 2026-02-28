# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.c : algo with strings (made by gemini3 from py version)
  - c     : 1.961 seconds (3x, 1.953><1.977)

sudoku.go : algo with strings
  - go    : 16.664 seconds (228x, 14.170><17.145)

sudoku.java : algo with strings
  - java  : 27.139 seconds (29x, 20.867><29.783)

sudoku.js : algo with strings
  - node  : 30.222 seconds (36x, 27.289><32.321)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 22.714 seconds (82x, 21.943><24.433)

sudoku.nim : algo with strings
  - nim   : 23.237 seconds (76x, 22.693><24.379)

sudoku.php : algo with strings
  - php   : 82.379 seconds (31x, 69.539><85.411)

sudoku.py : algo with strings
  - codon : 13.484 seconds (20x, 12.449><13.650)
  - py3   : 88.216 seconds (228x, 85.878><93.138)
  - pypy  : 18.956 seconds (460x, 17.714><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 8.452 seconds (3x, 8.421><8.585)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.c : algo OPTIMIZED (by copilot)
  - c     : 0.130 seconds (3x, 0.130><0.130)

specialized/sudoku.go : algo with arrays (optimized by copilot)
  - go    : 2.233 seconds (78x, 2.218><2.423)

specialized/sudoku.nim : algo with specialized types using bitsets (optimized by copilot)
  - nim   : 1.091 seconds (76x, 1.038><1.144)

specialized/sudoku.py : algo with specialized types/logics (optimized by copilot)
  - codon : 0.816 seconds (20x, 0.806><0.869)
  - py3   : 16.484 seconds (76x, 14.539><17.648)
  - pypy  : 1.097 seconds (76x, 1.060><1.167)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.681 seconds (3x, 0.681><0.684)

specialized/sudoku2.go : from c to go (by gemini3)
  - go    : 0.375 seconds (71x, 0.365><0.431)

specialized/sudoku2.nim : from c to nim (by gemini3)
  - nim   : 0.225 seconds (71x, 0.219><0.255)

specialized/sudoku2.py : conversion from C to py3 (by gemini3)
  - codon : 1.040 seconds (20x, 1.009><1.071)
  - py3   : 11.973 seconds (72x, 10.999><13.681)
  - pypy  : 2.787 seconds (72x, 2.760><3.517)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.14.0-1017-azure-x86_64-with-glibc2.39 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.86 bogomips)
MEMINFO  : 16374252 kB

c     : gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
        /usr/bin/gcc -O3 <file> -o ./sudoku && ./sudoku < grids.txt
codon : 0.19.5
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.22.2 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 17.0.18 2026-01-20
        /usr/bin/javac -d . <file> && /usr/bin/java Sudoku < grids.txt
mojo  : Mojo 0.25.7.0 (e5af2b2f)
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.16 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger -o:sudoku <file> && ./sudoku < grids.txt
node  : v20.20.0
        /usr/local/bin/node <file> < grids.txt
php   : PHP 8.3.30 (cli) (built: Jan 26 2026 22:59:51) (NTS)
        /usr/bin/php <file> < grids.txt
py3   : Python 3.12.3
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.93.1 (01f6ddf75 2026-02-11)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


