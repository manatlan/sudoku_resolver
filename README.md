Here is the **simplest|minimal|readable** python3 resolver (naive backtracing, recursive):

```python
sqr   = lambda g,x,y: g[y*9+x:y*9+x+3] + g[y*9+x+9:y*9+x+12] + g[y*9+x+18:y*9+x+21]
col   = lambda g,x:   g[x::9]
row   = lambda g,y:   g[y*9:y*9+9]
free  = lambda g,x,y: set("123456789") - set(col(g,x) + row(g,y) + sqr(g,(x//3)*3,(y//3)*3))

def resolv(g):
    i=g.find(".")
    if i>=0:
        for elem in free(g,i%9,i//9):
            ng=resolv( g[:i] + elem + g[i+1:] )
            if ng: return ng
    else:
        return g
```

Some grids are available in `g_simples.txt` (a grid by line of 81 chars, empty cases are `.`)

The idea of the repo, is to compare differents languages at "run times". Currently, there a c/mojo/nim/java/js versions. So every version implements the same algorithm, without using specials optimisations provided by the language itself (I known that the mojo version with SIMD could outperform the C version)... and try to resolve the **first 100 grids**  !

On my computer (Intel® N100 × 4 / ubuntu 23.10), I got :

```
node18.13:  0m 44s

py3.7:      0m 40s
py3.11:     0m 34s
pypy3.10:   0m 15s
codon0.16:  0m 23s

java:       0m 21s (openjdk 22)

Nim1.6.14:  0m 11s (release mode)
Nim1.6.14:  0m 8s (danger mode)

mojo0.4.0:  0m 6.5s (sudoku.mojo)

c/gcc    :  0m 2.7s
```

BTW, Other mojo results :

```
mojo0.4.0:  0m 3.6s (mojos/sudoku_optim.mojo) (same algo)
mojo0.4.0:  0m 2s (mojos/dojo.mojo) (different algo)
```