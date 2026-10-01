# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.c : algo with strings (made by gemini3 from py version)
  - c     : 1.961 seconds (214x, 1.338><2.502)

sudoku.go : algo with strings
  - go    : 16.657 seconds (439x, 8.639><18.214)

sudoku.java : algo with strings
  - java  : 26.890 seconds (35x, 14.212><29.638)

sudoku.js : algo with strings
  - node  : 28.623 seconds (1x, 28.623><28.623)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 22.472 seconds (248x, 12.199><24.433)

sudoku.nim : algo with strings
  - nim   : 23.263 seconds (287x, 12.302><26.146)

sudoku.php : algo with strings
  - php   : 80.101 seconds (8x, 50.680><81.190)

sudoku.py : algo with strings
  - codon : 29.387 seconds (3x, 23.208><29.591)
  - py3   : 87.926 seconds (439x, 44.890><99.134)
  - pypy  : 18.775 seconds (671x, 9.966><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 4.405 seconds (22x, 2.780><4.580)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.c : algo OPTIMIZED (by copilot)
  - c     : 0.130 seconds (214x, 0.103><0.155)

specialized/sudoku.go : algo with arrays (optimized by copilot)
  - go    : 2.237 seconds (289x, 1.426><2.582)

specialized/sudoku.nim : algo with specialized types using bitsets (optimized by copilot)
  - nim   : 1.094 seconds (287x, 0.661><1.287)

specialized/sudoku.py : algo with specialized types/logics (optimized by copilot)
  - codon : 0.825 seconds (3x, 0.649><0.826)
  - py3   : 16.543 seconds (287x, 8.561><17.875)
  - pypy  : 1.109 seconds (287x, 0.572><1.384)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.706 seconds (22x, 0.456><0.814)

specialized/sudoku2.go : from c to go (by gemini3)
  - go    : 0.377 seconds (282x, 0.252><0.455)

specialized/sudoku2.nim : from c to nim (by gemini3)
  - nim   : 0.226 seconds (282x, 0.173><0.280)

specialized/sudoku2.py : conversion from C to py3 (by gemini3)
  - codon : 0.854 seconds (3x, 0.689><0.858)
  - py3   : 11.960 seconds (283x, 6.333><14.543)
  - pypy  : 2.805 seconds (283x, 1.596><3.517)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.17.0-1022-azure-x86_64-with-glibc2.39 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.85 bogomips)
MEMINFO  : 16373452 kB

c     : gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
        /usr/bin/gcc -O3 <file> -o ./sudoku && ./sudoku < grids.txt
codon : 0.20.3
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.22.2 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 17.0.20.1 2026-08-18
        /usr/bin/javac -d . <file> && /usr/bin/java Sudoku < grids.txt
mojo  : Mojo 0.25.7.0 (e5af2b2f)
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.16 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger -o:sudoku <file> && ./sudoku < grids.txt
node  : v22.23.3
        /usr/local/bin/node <file> < grids.txt
php   : PHP 8.3.35 (cli) (built: Sep 23 2026 11:56:59) (NTS)
        /usr/bin/php <file> < grids.txt
py3   : Python 3.12.3
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.98.1 (48a229cea 2026-09-01)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


