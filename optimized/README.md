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
 optimized/sudoku.mojo : the optimized algo, with strings (1956grids)
  - mojo  : 61.52 seconds (6x, 58.75><64.56)

 optimized/sudoku.py : the optimized algo, with strings (1956grids)
  - codon : 92.2 seconds (6x, 91.61><98.41)
  - py311 : 135.5 seconds (6x, 124.15><140.54)
  - py37  : 204.33 seconds (6x, 183.92><279.88)
  - pypy  : 94.1 seconds (6x, 87.95><97.18)

 optimized/sudoku.java : the optimized algo, with strings (1956grids)
  - java  : 103.54 seconds (6x, 99.33><122.73)





 optimized/sudoku_specialized.mojo : optimized algo, with specialized types (1956grids)
  - mojo  : 3.59 seconds (19x, 3.57><3.70)

 optimized/sudoku_specialized_parallel.mojo : optimized algo, with specialized types & parallelization (1956grids)
  - mojo  : 1.22 seconds (19x, 1.18><1.41)

 optimized/sudoku_specialized.rs : the optimized algo, with specialized types (and readable) (1956grids)
  - rust  : 1.085 seconds (9x, 1.075><1.134)

```


