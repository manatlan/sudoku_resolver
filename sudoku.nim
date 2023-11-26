#!./make.py
#INFO: the simple algo, with strings (100grids)


############################################### my resolver ;-) (backtracking)
proc sqr( g:string, x:int, y:int ): string =
    let x = (x div 3)*3
    let y = (y div 3)*3
    g[y*9+x .. y*9+x+2] & g[y*9+x+9 .. y*9+x+11] & g[y*9+x+18 .. y*9+x+20]

proc col( g:string, x:int ): string =
    result = ""
    for y in 0 .. 8:
        result.add g[ y*9 + x]

proc row( g:string, y:int ): string =
    g[y*9 .. y*9 + 8]

proc freeset( sg:string) : set[char] =
    result = {'1'..'9'}
    for c in sg: result.excl c

proc free( g:string, x:int, y:int ): set[char] =
    freeset(row(g,y) & col(g,x) & sqr(g,x,y))

proc resolv( g:string ): string =
    let i = g.find('.')
    if i>=0:
        for elem in free(g, i mod 9, i div 9):
            let ng = resolv( g[0..i-1] & elem & g[i+1..80] )
            if ng != "": return ng
    else:
        return g
###############################################
import strutils
import times

let gg = readFile("grids.txt").splitLines()[0..99]

let t = cpuTime()
for g in gg:
    echo resolv(g)

