# Results from 'GITHUB' host

The goal is to compare runtime speed of a same algo (sudoku resolver), in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Regular Results

All implementations use same bases types (string)

```

sudoku.go : algo with strings
  - go    : 16.670 seconds (62x, 16.588><16.955)

sudoku.java : algo with strings
  - java  : 27.137 seconds (44x, 26.595><30.771)

sudoku.js : algo with strings
  - node  : 30.385 seconds (18x, 30.051><31.316)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 80.739 seconds (210x, 78.375><86.289)

sudoku.nim : algo with strings
  - nim   : 23.311 seconds (80x, 22.279><24.479)

sudoku.php : ?
  - php   : 82.541 seconds (1x, 82.541><82.541)

sudoku.py : algo with strings
  - codon : 13.529 seconds (32x, 13.387><13.837)
  - py3   : 88.730 seconds (62x, 86.923><93.035)
  - pypy  : 19.069 seconds (294x, 18.240><36.082)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 8.003 seconds (18x, 7.957><8.118)

```

## Specialized Results

It's the same algorithm, but use specialized weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.649 seconds (18x, 0.645><0.667)

```
## Context

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.8.0-1021-azure-x86_64-with-glibc2.39 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.85 bogomips)
MEMINFO  : 16373796 kB

codon : 0.18.1
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
go    : go version go1.22.2 linux/amd64
        /usr/bin/go build -o ./sudoku <file>  && ./sudoku < grids.txt
java  : openjdk 17.0.14 2025-01-21
        /usr/bin/javac <file> && /usr/bin/java Sudoku < grids.txt
mojo  : mojo 24.4.0 (2cb57382)
        /home/runner/.modular/pkg/packages.modular.com_mojo/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.14 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger <file> && ./sudoku < grids.txt
node  : v20.18.3
        /usr/local/bin/node <file> < grids.txt
php   : PHP 8.3.17 (cli) (built: Feb 28 2025 18:16:47) (NTS)
        /usr/bin/php <file> < grids.txt
py3   : Python 3.12.3
        /usr/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
        /opt/hostedtoolcache/PyPy/3.9.19/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.85.0 (4d91de4e4 2025-02-17)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```


