# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.c : algo with strings (made by gemini3 from py version)
  - c     : 1.952 seconds (20x, 1.949><2.168)

sudoku.go : algo with strings
  - go    : 16.666 seconds (245x, 14.170><17.145)

sudoku.java : algo with strings
  - java  : 27.118 seconds (46x, 20.867><30.332)

sudoku.js : algo with strings
  - node  : 31.113 seconds (3x, 27.621><31.769)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 22.714 seconds (98x, 21.943><24.433)

sudoku.nim : algo with strings
  - nim   : 23.242 seconds (93x, 22.693><24.379)

sudoku.php : algo with strings
  - php   : 82.377 seconds (48x, 69.539><85.411)

sudoku.py : algo with strings
  - codon : 13.566 seconds (14x, 12.565><13.664)
  - py3   : 88.165 seconds (245x, 85.878><93.138)
  - pypy  : 18.947 seconds (477x, 17.714><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 4.306 seconds (3x, 4.300><4.354)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.c : algo OPTIMIZED (by copilot)
  - c     : 0.130 seconds (20x, 0.129><0.147)

specialized/sudoku.go : algo with arrays (optimized by copilot)
  - go    : 2.233 seconds (95x, 2.218><2.423)

specialized/sudoku.nim : algo with specialized types using bitsets (optimized by copilot)
  - nim   : 1.092 seconds (93x, 1.038><1.287)

specialized/sudoku.py : algo with specialized types/logics (optimized by copilot)
  - codon : 0.821 seconds (14x, 0.809><0.881)
  - py3   : 16.555 seconds (93x, 14.539><17.648)
  - pypy  : 1.098 seconds (93x, 1.060><1.167)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.695 seconds (3x, 0.691><0.704)

specialized/sudoku2.go : from c to go (by gemini3)
  - go    : 0.375 seconds (88x, 0.365><0.431)

specialized/sudoku2.nim : from c to nim (by gemini3)
  - nim   : 0.226 seconds (88x, 0.219><0.255)

specialized/sudoku2.py : conversion from C to py3 (by gemini3)
  - codon : 1.038 seconds (14x, 1.032><1.085)
  - py3   : 11.933 seconds (89x, 10.999><13.681)
  - pypy  : 2.787 seconds (89x, 2.760><3.517)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.14.0-1017-azure-x86_64-with-glibc2.39 with 4 cpus
CPUINFO  : GenuineIntel "Intel(R) Xeon(R) Platinum 8370C CPU @ 2.80GHz" (5587.06 bogomips)
MEMINFO  : 16377516 kB

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


