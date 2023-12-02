# Results from 'GITHUB' host

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
PLATFORM : x86_64/Linux-6.2.0-1016-azure-x86_64-with-glibc2.35 with 4 cpus
CPUINFO  : AuthenticAMD "AMD EPYC 7763 64-Core Processor" (4890.87 bogomips)
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
  - java  : 22.516 seconds (11x, 22.136><22.790)

sudoku.js : algo with strings
  - node  : 29.643 seconds (11x, 29.531><30.638)

sudoku.mojo : algo with strings (use python to read stdin)
  - mojo  : 83.080 seconds (11x, 81.576><84.931)

sudoku.nim : algo with strings
  - nim   : 23.815 seconds (11x, 23.325><25.014)

sudoku.py : algo with strings
  - codon : 12.204 seconds (9x, 12.101><12.353)
  - py3   : 103.600 seconds (9x, 102.520><104.085)
  - pypy  : 19.712 seconds (9x, 19.177><19.963)

sudoku.rs : algo with Strings (as byte[])
  - rust  : 8.720 seconds (3x, 8.703><8.845)

```

## Specialized

It's the same algorithm, but use weapons (types/apis) from the languages, to be as faster as possible.

```

specialized/sudoku.mojo : algo with specialized types (use python to read stdin)
  - mojo  : 1.731 seconds (11x, 1.713><1.762)

specialized/sudoku.rs : algo with specialized types
  - rust  : 0.623 seconds (11x, 0.616><0.626)

```


