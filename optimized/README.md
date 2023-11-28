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
optimized/sudoku.java : the optimized algo, with strings (1956grids)
  - java  : 104.434 seconds (5x, 96.915><106.195)

optimized/sudoku.mojo : the optimized algo, with strings (1956grids)
  - mojo  : 63.204 seconds (5x, 62.332><68.250)

optimized/sudoku.py : the optimized algo, with strings (1956grids)
  - py3   : 130.611 seconds (5x, 119.809><138.367)
  - pypy  : 88.693 seconds (5x, 86.168><92.982)
  - codon : 95.918 seconds (5x, 94.827><108.770)
  - py37  : 193.619 seconds (5x, 158.285><202.944)



optimized/sudoku_specialized.mojo : optimized algo, with specialized types (1956grids)
  - mojo  : 3.733 seconds (5x, 3.726><3.905)

optimized/sudoku_specialized.rs : the optimized algo, with specialized types (and readable) (1956grids)
  - rust  : 1.603 seconds (5x, 1.598><2.015)

optimized/sudoku_specialized_parallel.mojo : optimized algo, with specialized types & parallelization (1956grids)
  - mojo  : 1.337 seconds (5x, 1.312><1.477)

```


