# Results from 'GITHUB' host

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.2.0-1016-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.85 bogomips)
MEMINFO  : 16365020 kB

codon : 0.16.3
        /home/runner/.codon/bin/codon build -release <file> -o ./sudoku && ./sudoku < grids.txt
java  : openjdk 11.0.21 2023-10-17
        /usr/bin/javac <file> && /usr/bin/java Sudoku < grids.txt
mojo  : mojo 0.5.0 (6e50a738)
        /home/runner/.modular/pkg/packages.modular.com_mojo/bin/mojo build <file> -o ./sudoku && ./sudoku < grids.txt
nim   : Nim Compiler Version 2.0.0 [Linux: amd64]
        /home/runner/.nimble/bin/nim compile -d:danger <file> && ./sudoku < grids.txt
node  : v18.18.2
        /usr/local/bin/node <file> < grids.txt
py3   : Python 3.10.12
        /usr/bin/python3 -uOO <file> < grids.txt
pypy  : Python 3.9.18 (c5262994620471e725f57d652d78d842270649d6, Sep 27 2023, 13:43:44)
        /opt/hostedtoolcache/PyPy/3.9.18/x64/bin/pypy3 -uOO <file> < grids.txt
rust  : rustc 1.74.0 (79e9716c9 2023-11-13)
        /home/runner/.cargo/bin/rustc -C opt-level=3 -C target-cpu=native <file> -o ./sudoku && ./sudoku < grids.txt

```

The goal is to compare runtime speed of a same algo, in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Results

All implementations use same bases types (string)

```

sudoku.java : algo with strings
  - java  : 22.406 seconds (3x, 22.136><22.516)

sudoku.js : algo with strings
  - node  : 29.793 seconds (3x, 29.611><29.952)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 82.272 seconds (3x, 81.576><83.838)

sudoku.nim : algo with strings
  - nim   : 23.887 seconds (3x, 23.590><24.119)

sudoku.py : algo with strings
  - codon : 12.215 seconds (1x, 12.215><12.215)
  - py3   : 103.993 seconds (1x, 103.993><103.993)
  - pypy  : 19.620 seconds (1x, 19.620><19.620)

sudoku.rs : algo with Strings (as byte[]) !!!! NOT OPTIMAL !!!!
  - rust  : 13.310 seconds (3x, 13.289><13.353)

```

## Specialized

It's the same algorithm, but use weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.mojo : algo with specialized types (use python to read stdin)
  - mojo  : 1.738 seconds (3x, 1.715><1.739)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.623 seconds (3x, 0.616><0.623)

```


