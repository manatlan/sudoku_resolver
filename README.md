Just a repo to hold the code ...

`sudoku.py` is my sudoku resolver in python (13 lines)

`sudoku.nim` is my [nim](https://nim-lang.org/) version

`sudoku.mojo` is my [mojo](https://www.modular.com/mojo) version

Some grids are available in `g_simples.txt`

Nim version is really quick compared to py one ...
(just test the first 100 over the 1011)

On my old computer (Intel® Core™ i3 CPU 530 @ 2.93GHz × 4), for the first 100 grids :

```
py3.8:   2m 05s
pypy:    0m 58s

java:    0m 50s (openjdk)

Nim:     2m 53s (normal mode (debug)) !?!?
Nim:     0m 19s (release mode)
Nim:     0m 16s (danger mode)
```

On my new computer (Intel® N100 × 4), for the first 100 grids :
(freeset method was optimized for all versions)

```
node18.13:  0m 44s

py3.7:      0m 45s
py3.11:     0m 35s
pypy3.10:   0m 15s

java:       0m 21s (openjdk 22)

Nim1.6.14:  0m 11s (release mode)
Nim1.6.14:  0m 8s (danger mode)

mojo0.4.0:  0m 7s

```