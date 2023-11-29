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

And now, they are resolving all the grids in [grids.txt](../grids.txt) : **1956 grids** (some are really complex too)

On my computer (Intel® N100 × 4 / ubuntu 23.10), I got :

```
optimized/sudoku.java : the optimized algo, with strings (1956grids)
  - java  : 33.022 seconds (5x, 32.402><33.822)

optimized/sudoku.mojo : the optimized algo, with strings (1956grids)
  - mojo  : 64.017 seconds (10x, 62.332><68.250)

optimized/sudoku.py : the optimized algo, with strings (1956grids)
  - py3   : 96.048 seconds (4x, 95.176><100.762)
  - pypy  : 39.315 seconds (4x, 38.107><40.982)
  - codon : 26.791 seconds (4x, 26.008><27.569)
  - py37  : 142.193 seconds (3x, 141.189><145.208)





optimized/sudoku_specialized.mojo : optimized algo, with specialized types (1956grids)
  - mojo  : 3.751 seconds (8x, 3.726><3.905)

optimized/sudoku_specialized.rs : the optimized algo, with specialized types (and readable) (1956grids)
  - rust  : 1.602 seconds (8x, 1.586><2.015)

optimized/sudoku_specialized_parallel.mojo : optimized algo, with specialized types & parallelization (1956grids)
  - mojo  : 1.401 seconds (8x, 1.312><1.548)

```


