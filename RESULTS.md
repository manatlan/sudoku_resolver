# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.c : algo with strings (made by gemini3 from py version)
  - c     : 1.474 seconds (2x, 1.365><1.582)

sudoku.go : algo with strings
  - go    : 10.458 seconds (2x, 10.316><10.601)

sudoku.java : algo with strings
  - java  : 19.031 seconds (2x, 17.595><20.466)

sudoku.js : algo with strings
  - node  : 22.361 seconds (1x, 22.361><22.361)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 22.424 seconds (284x, 12.199><24.433)

sudoku.nim : algo with strings
  - nim   : 23.249 seconds (325x, 12.302><26.146)

sudoku.php : algo with strings
  - php   : 58.620 seconds (2x, 54.176><63.064)

sudoku.py : algo with strings
  - py3   : 56.935 seconds (2x, 52.848><61.022)
  - pypy  : 18.776 seconds (709x, 9.966><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 4.298 seconds (17x, 2.771><4.371)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.c : algo OPTIMIZED (by copilot)
  - c     : 0.104 seconds (2x, 0.104><0.104)

specialized/sudoku.go : algo with arrays (optimized by copilot)
  - go    : 1.891 seconds (2x, 1.810><1.972)

specialized/sudoku.nim : algo with specialized types using bitsets (optimized by copilot)
  - nim   : 1.094 seconds (325x, 0.661><1.287)

specialized/sudoku.py : algo with specialized types/logics (optimized by copilot)
  - codon : 0.751 seconds (14x, 0.521><0.887)
  - py3   : 10.963 seconds (2x, 9.906><12.020)
  - pypy  : 1.111 seconds (325x, 0.572><1.384)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.738 seconds (17x, 0.484><0.802)

specialized/sudoku2.go : from c to go (by gemini3)
  - go    : 0.277 seconds (2x, 0.273><0.282)

specialized/sudoku2.nim : from c to nim (by gemini3)
  - nim   : 0.226 seconds (320x, 0.173><0.280)

specialized/sudoku2.py : conversion from C to py3 (by gemini3)
  - codon : 0.814 seconds (14x, 0.600><0.905)
  - py3   : 8.079 seconds (2x, 7.619><8.539)
  - pypy  : 2.806 seconds (321x, 1.596><3.582)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : /Linux-7.0.0-1016-aws-x86_64-with-glibc2.43 with 4 cpus
CPUINFO  : GenuineIntel "Intel(R) Xeon(R) 6975P-C" (5400.00 bogomips)
MEMINFO  : 16077548 kB

c     : gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0
        /usr/bin/gcc -O3 <file> -o ./sudoku && ./sudoku < grids.txt
codon : 0.20.6
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
php   : PHP 8.3.36 (cli) (built: Oct 24 2026 12:11:20) (NTS)
        /usr/bin/php <file> < grids.txt
py3   : Python 3.12.16
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.99.1 (58cf8f9c3 2026-10-13)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


