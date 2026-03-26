# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.c : algo with strings (made by gemini3 from py version)
  - c     : 1.953 seconds (28x, 1.949><2.172)

sudoku.go : algo with strings
  - go    : 16.666 seconds (253x, 14.170><17.145)

sudoku.java : algo with strings
  - java  : 27.104 seconds (54x, 20.867><30.332)

sudoku.js : algo with strings
  - node  : 30.172 seconds (11x, 27.531><31.769)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 22.714 seconds (104x, 21.943><24.433)

sudoku.nim : algo with strings
  - nim   : 23.259 seconds (101x, 22.693><24.381)

sudoku.php : algo with strings
  - php   : 82.332 seconds (56x, 69.539><85.411)

sudoku.py : algo with strings
  - codon : 13.590 seconds (22x, 12.504><13.817)
  - py3   : 88.173 seconds (253x, 85.878><93.138)
  - pypy  : 18.942 seconds (485x, 17.578><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 4.312 seconds (11x, 4.300><4.450)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.c : algo OPTIMIZED (by copilot)
  - c     : 0.130 seconds (28x, 0.129><0.147)

specialized/sudoku.go : algo with arrays (optimized by copilot)
  - go    : 2.234 seconds (103x, 2.218><2.427)

specialized/sudoku.nim : algo with specialized types using bitsets (optimized by copilot)
  - nim   : 1.092 seconds (101x, 1.038><1.287)

specialized/sudoku.py : algo with specialized types/logics (optimized by copilot)
  - codon : 0.822 seconds (22x, 0.809><0.881)
  - py3   : 16.560 seconds (101x, 14.539><17.648)
  - pypy  : 1.098 seconds (101x, 1.044><1.167)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.697 seconds (11x, 0.690><0.744)

specialized/sudoku2.go : from c to go (by gemini3)
  - go    : 0.376 seconds (96x, 0.365><0.435)

specialized/sudoku2.nim : from c to nim (by gemini3)
  - nim   : 0.226 seconds (96x, 0.219><0.255)

specialized/sudoku2.py : conversion from C to py3 (by gemini3)
  - codon : 1.041 seconds (22x, 1.032><1.085)
  - py3   : 11.945 seconds (97x, 10.999><13.681)
  - pypy  : 2.788 seconds (97x, 2.760><3.517)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.14.0-1017-azure-x86_64-with-glibc2.39 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.86 bogomips)
MEMINFO  : 16374252 kB

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
node  : v20.20.1
        /usr/local/bin/node <file> < grids.txt
php   : PHP 8.3.30 (cli) (built: Jan 26 2026 22:59:51) (NTS)
        /usr/bin/php <file> < grids.txt
py3   : Python 3.12.3
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.94.0 (4a4ef493e 2026-03-02)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


