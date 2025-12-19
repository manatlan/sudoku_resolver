# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.c : algo with strings (made by gemini3 from py version)
  - c     : 1.965 seconds (3x, 1.947><2.173)

sudoku.go : algo with strings
  - go    : 16.669 seconds (157x, 15.152><17.145)

sudoku.java : algo with strings
  - java  : 26.917 seconds (4x, 24.075><27.372)

sudoku.js : algo with strings
  - node  : 30.214 seconds (14x, 27.908><31.199)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 22.607 seconds (14x, 22.046><23.538)

sudoku.nim : algo with strings
  - nim   : 22.923 seconds (5x, 22.735><23.322)

sudoku.php : algo with strings
  - php   : 82.234 seconds (14x, 69.074><82.950)

sudoku.py : algo with strings
  - codon : 13.816 seconds (14x, 12.655><14.065)
  - py3   : 88.508 seconds (157x, 86.241><93.138)
  - pypy  : 19.021 seconds (389x, 17.905><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 6.247 seconds (9x, 6.034><6.287)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.c : algo OPTIMIZED (by copilot)
  - c     : 0.135 seconds (2x, 0.130><0.141)

specialized/sudoku.go : algo with arrays (optimized by copilot)
  - go    : 2.233 seconds (7x, 2.222><2.365)

specialized/sudoku.nim : algo with specialized types using bitsets (optimized by copilot)
  - nim   : 1.093 seconds (5x, 1.042><1.095)

specialized/sudoku.py : algo with specialized types/logics (optimized by copilot)
  - codon : 0.818 seconds (5x, 0.809><0.862)
  - py3   : 16.154 seconds (5x, 14.720><16.223)
  - pypy  : 1.092 seconds (5x, 1.079><1.117)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.687 seconds (9x, 0.677><0.713)

specialized/sudoku2.py : conversion from C to py3 (by gemini3)
  - codon : 1.109 seconds (1x, 1.109><1.109)
  - py3   : 11.164 seconds (1x, 11.164><11.164)
  - pypy  : 3.517 seconds (1x, 3.517><3.517)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.11.0-1018-azure-x86_64-with-glibc2.39 with 4 cpus
CPUINFO  : GenuineIntel "Intel(R) Xeon(R) Platinum 8370C CPU @ 2.80GHz" (5586.87 bogomips)
MEMINFO  : 16378460 kB

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


