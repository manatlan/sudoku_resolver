#!./make.py
from time import now
from math import iota
from algorithm import parallelize
from sudoku_specialized import Grid
#INFO: the simple algo, with specialized types & parallelization

fn main() raises:
    let buf = open("grids.txt", "r").read()
    let t=now()

    @parameter
    fn in_p(i:Int):
        let g=Grid(buf[i*82:i*82+81])
        print( g.solve() and g.to_string() )

    parallelize[in_p](100,100) #more workers to distribute the effort on cores
    print("Took:",(now() - t)/1_000_000_000,"s")
    
    _=buf^ #extend lifetime of pointer
