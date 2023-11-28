#!/usr/bin/python3
import subprocess,sys,platform

tmpl_md="""
# Result on %s

```
%s
```

## Simple Algo

For the first 100 grids : At each iteration, they will resolve the first hole of the grid, til no holes.
(*specialized* versions use all weapons available in language, while others use string and hashset)
```
%s
```

## Optimized Algo

For **all 1956** grids : At each iteration, they will firstly resolve the hole, with minimal choices, of the grid, til no holes.
(*specialized* versions use all weapons available in language, while others use string and hashset)

```
%s
```

"""

def call_make(*args):
    cmd=[sys.executable, "make.py", *args]
    cp=subprocess.run(cmd,shell=False,text=True,capture_output=True)
    return cp.stdout

if __name__=="__main__":
    if sys.argv[1:]==["RESULTS"]:
        # STATS from RESULTS.TXT
        print( tmpl_md % (
            platform.node(),
            call_make("info"),
            call_make("RESULTS","."),
            call_make("RESULTS","optimized"),
        ))
    else:
        # STATS from live db
        print( tmpl_md % (
            platform.node(),
            call_make("info"),
            call_make("stats","."),
            call_make("stats","optimized"),
        ))
