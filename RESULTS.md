# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.go : algo with strings
  - go    : 16.672 seconds (109x, 16.564><17.145)

sudoku.java : algo with strings
  - java  : 27.115 seconds (9x, 26.862><27.750)

sudoku.js : algo with strings
  - node  : 30.340 seconds (2x, 30.319><30.360)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 80.739 seconds (210x, 78.375><86.289)

sudoku.nim : algo with strings
  - nim   : 23.326 seconds (10x, 22.930><23.738)

sudoku.php : algo with strings
  - php   : 83.902 seconds (19x, 82.348><85.165)

sudoku.py : algo with strings
  - codon : 13.220 seconds (44x, 12.891><13.839)
  - py3   : 88.645 seconds (109x, 86.923><93.035)
  - pypy  : 19.061 seconds (341x, 17.905><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 8.184 seconds (25x, 7.971><8.346)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.642 seconds (25x, 0.615><0.651)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.11.0-1012-azure-x86_64-with-glibc2.39 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.86 bogomips)
MEMINFO  : 16373456 kB

codon : 0.18.2
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.22.2 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 17.0.15 2025-04-15
        /usr/bin/javac <file> && /usr/bin/java Sudoku < grids.txt
mojo  : mojo 24.4.0 (2cb57382)
        /home/runner/.modular/pkg/packages.modular.com_mojo/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.16 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger <file> && ./sudoku < grids.txt
node  : v20.19.1
        /usr/local/bin/node <file> < grids.txt
php   : PHP 8.3.20 (cli) (built: Apr 13 2025 03:29:45) (NTS)
        /usr/bin/php <file> < grids.txt
py3   : Python 3.12.3
        /usr/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.86.0 (05f9846f8 2025-03-31)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


