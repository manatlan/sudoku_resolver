#!./make.py
from time import now
"""
this is "the simple algo, with strings" ... adapted for mojo 0.5 features (str.find).

If you are looking for mojo issue #1216 (https://github.com/modularml/mojo/issues/1216)

the old code (dev for mojo0.4) is here:
https://github.com/manatlan/sudoku_resolver/blob/mojo_0.4.0/sudoku.mojo
(this [^^] was a lot faster (10x) using mojo0.4 than mojo0.5 !!!!)
(and this [^^] is faster (2x) than this code [vv] with mojo0.5.0)
"""

#INFO: the simple algo, with strings (100grids)
alias ALL = StringRef("123456789")

fn sqr(g:String,x:Int,y:Int) -> String:
    return g[y*9+x:y*9+x+3] + g[y*9+x+9:y*9+x+12] + g[y*9+x+18:y*9+x+21]
fn col(g:String,x:Int) -> String:
    return g[x::9]
fn row(g:String,y:Int) -> String:
    return g[y*9:y*9+9]
fn free(g:String,x:Int,y:Int) -> String:
    let t27=col(g,x) + row(g,y) + sqr(g,(x//3)*3,(y//3)*3)
    var freeset = String("")
    for i in range(len(ALL)):
        if t27.find(ALL[i])<0:
            freeset += ALL[i]
    return freeset

fn resolv(g: String) -> String:
    let i=g.find(".")
    if i>=0:
        let x=free(g,i%9,i//9)
        for idx in range(len(x)):
            let ng=resolv( g[:i] + x[idx] + g[i+1:] )
            if ng: return ng
        return ""
    else:
        return g

fn main() raises:
    let buf = open("grids.txt", "r").read()
    for i in range(100):
        print(resolv(buf[i*82:i*82+81]))
