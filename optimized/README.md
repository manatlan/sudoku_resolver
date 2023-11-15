# the "optimized" algo

Basically the same thing, but with **a big improvment** on the algorithm, which makes them a lot faster 

Here is the python version, it's the same algo but with a new constraint "choosing the most constrained digit each iteration" (thanks to [2e71828](https://users.rust-lang.org/u/2e71828))
:

```python

sqr   = lambda g,x,y: g[y*9+x:y*9+x+3] + g[y*9+x+9:y*9+x+12] + g[y*9+x+18:y*9+x+21]
col   = lambda g,x:   g[x::9]
row   = lambda g,y:   g[y*9:y*9+9]
free  = lambda g,x,y: set("123456789") - set(col(g,x) + row(g,y) + sqr(g,(x//3)*3,(y//3)*3))

def resolv(g):
    holes={}
    for i in range(81):
        if g[i]==".":
            holes[i]=free(g,i % 9, i // 9)
            if len(holes[i])==1: break
    if holes: 
        i,avails = sorted( holes.items() , key=lambda x: len(x[1])).pop(0)
        for c in avails:
            ng = resolv( g[:i] + c + g[i+1:] )
            if ng: return ng
    else:
        return g
```

And now, they are resolving all the grids in `g_simples.txt` : **1956 grids** (some are really complex too)

On my computer (Intel® N100 × 4 / ubuntu 23.10), I got :

```

optimized/sudoku_specialized.mojo (optimized algo, with specialized types)
 - mojo  : 3.60 seconds

optimized/sudoku_specialized_parallel.mojo (optimized algo, with specialized types & parallelization)
 - mojo  : 2.28 seconds

optimized/sudoku_specialized.rs (the optimized algo, with ultra-specialized types/api)
 - rust  : 3.87 seconds





optimized/sudoku.java (the optimized algo, with strings)
 - java  : 105.35 seconds

optimized/sudoku.py (the optimized algo, with strings)
 - codon : 94.89 seconds
 - pypy  : 95.68 seconds
 - py311 : 135.56 seconds
 - py37  : 197.21 seconds

optimized/sudoku.mojo (the optimized algo, with strings)
 - mojo  : 61.43 seconds

```


