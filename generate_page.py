#!/usr/bin/python3
import subprocess,sys,platform

tmpl_md="""# Results from '%s' host

Here are informations about the host/computer, and languages/versions/cmdline used for tests:
```
%s
```

The goal is to compare runtime speed of a same algo, in differents implementations/languages, while injecting the 1956 grids of [grids.txt](grids.txt)

## Results

All implementations use same bases types (string)

```
%s
```

## Specialized

It's the same algorithm, but use weapons (types/apis) from the languages, to be as faster as possible.

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
            "GITHUB",
            call_make("info"),
            call_make("RESULTS","."),
            call_make("RESULTS","specialized"),
        ))
    else:
        # STATS from live db
        print( tmpl_md % (
            platform.node(),
            call_make("info"),
            call_make("stats","."),
            call_make("stats","specialized"),
        ))
