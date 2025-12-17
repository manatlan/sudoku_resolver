# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.go : algo with strings
  - go    : 16.671 seconds (148x, 16.564><17.145)

sudoku.java : algo with strings
  - java  : 27.154 seconds (5x, 26.916><29.934)

sudoku.js : algo with strings
  - node  : 30.453 seconds (5x, 30.051><30.988)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 22.483 seconds (5x, 22.134><22.786)

sudoku.nim : algo with strings
  - nim   : 23.468 seconds (49x, 22.917><24.156)

sudoku.php : algo with strings
  - php   : 82.668 seconds (5x, 81.623><82.845)

sudoku.py : algo with strings
  - codon : 13.808 seconds (5x, 13.706><13.902)
  - py3   : 88.542 seconds (148x, 86.366><93.035)
  - pypy  : 19.036 seconds (380x, 17.905><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 12.261 seconds (5x, 12.225><12.293)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.694 seconds (5x, 0.688><0.701)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.11.0-1018-azure-x86_64-with-glibc2.39 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.86 bogomips)
MEMINFO  : 16379472 kB

codon : 0.19.4
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.22.2 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 17.0.17 2025-10-21
        /usr/bin/javac <file> && /usr/bin/java Sudoku < grids.txt
mojo  : Mojo 0.25.7.0 (e5af2b2f)
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.16 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger <file> && ./sudoku < grids.txt
node  : v20.19.6
        /usr/local/bin/node <file> < grids.txt
php   : PHP 8.3.28 (cli) (built: Dec  9 2025 12:37:08) (NTS)
        /usr/bin/php <file> < grids.txt
py3   : Python 3.12.3
        /home/runner/work/sudoku_resolver/sudoku_resolver/.venv/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.91.1 (ed61e7d7e 2025-11-07)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


