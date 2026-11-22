# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.c : algo with strings (made by gemini3 from py version)
  - c     : 1.601 seconds (9x, 1.107><1.844)

sudoku.go : algo with strings
  - go    : 10.343 seconds (9x, 8.901><15.616)

sudoku.java : algo with strings
  - java  : 20.365 seconds (9x, 14.646><28.169)

sudoku.js : algo with strings
  - node  : 22.198 seconds (2x, 15.466><28.930)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 22.424 seconds (284x, 12.199><24.433)

sudoku.nim : algo with strings
  - nim   : 23.238 seconds (332x, 12.302><26.146)

sudoku.php : algo with strings
  - php   : 67.659 seconds (1x, 67.659><67.659)

sudoku.py : algo with strings
  - py3   : 61.417 seconds (9x, 46.314><87.637)
  - pypy  : 18.774 seconds (716x, 9.966><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 3.850 seconds (2x, 3.002><4.698)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.c : algo OPTIMIZED (by copilot)
  - c     : 0.104 seconds (9x, 0.098><0.139)

specialized/sudoku.go : algo with arrays (optimized by copilot)
  - go    : 1.819 seconds (9x, 1.483><2.542)

specialized/sudoku.nim : algo with specialized types using bitsets (optimized by copilot)
  - nim   : 1.094 seconds (332x, 0.661><1.287)

specialized/sudoku.py : algo with specialized types/logics (optimized by copilot)
  - codon : 0.660 seconds (5x, 0.527><0.883)
  - py3   : 12.060 seconds (9x, 8.365><15.509)
  - pypy  : 1.111 seconds (332x, 0.572><1.384)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.597 seconds (2x, 0.476><0.718)

specialized/sudoku2.go : from c to go (by gemini3)
  - go    : 0.282 seconds (9x, 0.248><0.368)

specialized/sudoku2.nim : from c to nim (by gemini3)
  - nim   : 0.226 seconds (327x, 0.173><0.280)

specialized/sudoku2.py : conversion from C to py3 (by gemini3)
  - codon : 0.692 seconds (5x, 0.584><0.898)
  - py3   : 8.616 seconds (9x, 6.448><11.957)
  - pypy  : 2.805 seconds (328x, 1.596><3.582)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : /Linux-7.0.0-1020-azure-x86_64-with-glibc2.43 with 4 cpus
CPUINFO  : GenuineIntel "INTEL(R) XEON(R) PLATINUM 8573C" (4599.99 bogomips)
MEMINFO  : 16365616 kB

c     : gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0
        /usr/bin/gcc -O3 <file> -o ./sudoku && ./sudoku < grids.txt
codon : 0.20.7
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.26.8 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 25.0.5 2026-10-20 LTS
        /usr/bin/javac -d . <file> && /usr/bin/java Sudoku < grids.txt
mojo  : Mojo 0.25.7.0 (e5af2b2f)
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.16 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger -o:sudoku <file> && ./sudoku < grids.txt
node  : v24.22.3
        /usr/local/bin/node <file> < grids.txt
php   : PHP 8.3.37 (cli) (built: Nov 21 2026 08:36:53) (NTS)
        /usr/bin/php <file> < grids.txt
py3   : Python 3.12.16
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.100.0 (0ef1bc386 2026-11-09)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


