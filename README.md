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

The idea of the repo, is to compare differents languages at "run times". Currently, there a c/mojo/nim/java/js/rust versions. So every version implements the same algorithm, without using specials optimisations provided by the language itself ... and try to resolve the **first 100 grids** !!!

On my computer (Intel® N100 × 4 / ubuntu 23.10), I got :

```
node18.13:  0m 45s

py3.7:      0m 48s
py3.11:     0m 29s
pypy3.10:   0m 15s
codon0.16:  0m 23s

java22:     0m 19s (openjdk)

Nim1.6.14:  0m 10s (danger mode)

mojo0.4.0:  0m 8s

c/gcc13.2:  0m 3s

rust1.71:   0m 24s/40s (not specialized version)

SPECIALIZED versions (with specialized types/structures by languages)
=====================
mojo0.4.0:  0m 2.5s (sudoku_specialized.mojo : with specialized types)
rust1.71:   0m 1.2s (sudoku_specialized.rs : with ultra-specialized rust types/apis)
```

BTW, Other experiments results :

```
mojo0.4.0:  0m 2s   (experiments/mojodojodev.mojo)  (different algo)
```

BTW2, tests with [an optimized algo](optimized) are availables too.