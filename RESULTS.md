# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.c : algo with strings (made by gemini3 from py version)
  - c     : 1.583 seconds (5x, 1.365><1.844)

sudoku.go : algo with strings
  - go    : 10.318 seconds (5x, 10.302><15.616)

sudoku.java : algo with strings
  - java  : 20.371 seconds (5x, 17.595><28.169)

sudoku.js : algo with strings
  - node  : 22.922 seconds (3x, 21.353><28.197)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 22.424 seconds (284x, 12.199><24.433)

sudoku.nim : algo with strings
  - nim   : 23.245 seconds (328x, 12.302><26.146)

sudoku.php : algo with strings
  - php   : 63.074 seconds (5x, 54.176><83.467)

sudoku.py : algo with strings
  - py3   : 61.128 seconds (5x, 52.848><87.637)
  - pypy  : 18.775 seconds (712x, 9.966><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 4.048 seconds (20x, 2.771><4.404)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.c : algo OPTIMIZED (by copilot)
  - c     : 0.104 seconds (5x, 0.104><0.115)

specialized/sudoku.go : algo with arrays (optimized by copilot)
  - go    : 1.817 seconds (5x, 1.807><2.088)

specialized/sudoku.nim : algo with specialized types using bitsets (optimized by copilot)
  - nim   : 1.094 seconds (328x, 0.661><1.287)

specialized/sudoku.py : algo with specialized types/logics (optimized by copilot)
  - codon : 0.660 seconds (1x, 0.660><0.660)
  - py3   : 12.060 seconds (5x, 9.906><15.509)
  - pypy  : 1.111 seconds (328x, 0.572><1.384)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.698 seconds (20x, 0.484><0.802)

specialized/sudoku2.go : from c to go (by gemini3)
  - go    : 0.282 seconds (5x, 0.268><0.321)

specialized/sudoku2.nim : from c to nim (by gemini3)
  - nim   : 0.226 seconds (323x, 0.173><0.280)

specialized/sudoku2.py : conversion from C to py3 (by gemini3)
  - codon : 0.687 seconds (1x, 0.687><0.687)
  - py3   : 8.616 seconds (5x, 7.619><11.957)
  - pypy  : 2.805 seconds (324x, 1.596><3.582)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : /Linux-7.0.0-1019-azure-x86_64-with-glibc2.43 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 9V74 80-Core Processor" (5192.29 bogomips)
MEMINFO  : 16366640 kB

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
node  : v24.22.2
        /usr/local/bin/node <file> < grids.txt
php   : PHP 8.3.36 (cli) (built: Oct 24 2026 12:11:20) (NTS)
        /usr/bin/php <file> < grids.txt
py3   : Python 3.12.16
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.99.1 (58cf8f9c3 2026-10-13)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


