# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.c : algo with strings (made by gemini3 from py version)
  - c     : 1.951 seconds (38x, 1.947><2.191)

sudoku.go : algo with strings
  - go    : 16.666 seconds (192x, 15.152><17.145)

sudoku.java : algo with strings
  - java  : 27.120 seconds (39x, 21.194><29.266)

sudoku.js : algo with strings
  - node  : 30.416 seconds (49x, 27.547><31.622)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 22.683 seconds (49x, 22.046><23.646)

sudoku.nim : algo with strings
  - nim   : 23.216 seconds (40x, 22.693><24.379)

sudoku.php : algo with strings
  - php   : 81.911 seconds (5x, 69.784><82.421)

sudoku.py : algo with strings
  - codon : 13.829 seconds (49x, 12.549><14.882)
  - py3   : 88.302 seconds (192x, 85.897><93.138)
  - pypy  : 18.980 seconds (424x, 17.905><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 6.245 seconds (44x, 6.030><6.383)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.c : algo OPTIMIZED (by copilot)
  - c     : 0.130 seconds (37x, 0.129><0.141)

specialized/sudoku.go : algo with arrays (optimized by copilot)
  - go    : 2.233 seconds (42x, 2.221><2.375)

specialized/sudoku.nim : algo with specialized types using bitsets (optimized by copilot)
  - nim   : 1.091 seconds (40x, 1.039><1.106)

specialized/sudoku.py : algo with specialized types/logics (optimized by copilot)
  - codon : 0.817 seconds (40x, 0.808><0.866)
  - py3   : 16.222 seconds (40x, 14.647><17.106)
  - pypy  : 1.092 seconds (40x, 1.060><1.167)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.683 seconds (44x, 0.676><0.713)

specialized/sudoku2.go : from c to go (by gemini3)
  - go    : 0.375 seconds (35x, 0.366><0.426)

specialized/sudoku2.nim : from c to nim (by gemini3)
  - nim   : 0.224 seconds (35x, 0.219><0.245)

specialized/sudoku2.py : conversion from C to py3 (by gemini3)
  - codon : 1.043 seconds (36x, 1.029><1.109)
  - py3   : 11.968 seconds (36x, 11.164><13.681)
  - pypy  : 2.788 seconds (36x, 2.762><3.517)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.11.0-1018-azure-x86_64-with-glibc2.39 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.85 bogomips)
MEMINFO  : 16379472 kB

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
php   : PHP 8.3.30 (cli) (built: Jan 17 2026 00:40:43) (NTS)
        /usr/bin/php <file> < grids.txt
py3   : Python 3.12.3
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.92.0 (ded5c06cf 2025-12-08)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


