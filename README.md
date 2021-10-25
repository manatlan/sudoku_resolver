Just a repo to hold the code ...

`sudoku.py` is my sudoku resolver in python (13 lines)

`sudoku.nim` is my nim version

Some grids are available in `g_simples.txt`

Nim version is really quick compared to py one ...
(just test the first 100 over the 1011)

On my old computer, for the 100 first grids :

```
py3:     2m 45s
nuitka3: 3m 26s
pypy:    1m 07s
Nim:     0m 16s (danger mode)
```