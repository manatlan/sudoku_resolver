#!./make.py --10
#INFO: algo with strings

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

proc free( g:string, x:int, y:int ): string =
    let t27=row(g,y) & col(g,x) & sqr(g,x,y)
    var freeset=""
    for c in "123456789":
        if t27.find(c)<0:
            freeset = freeset & c
    freeset    

proc resolv(g: string): string =
    var ibest = -1
    var cbest = "123456789"

    for i in 0 ..< 81:
        if g[i] == '.':
            let c = free(g, i mod 9, i div 9)
            if c.len == 0:
                return ""
            if c.len < cbest.len:
                ibest = i
                cbest = c
            if c.len == 1:
                break

    if ibest >= 0:
        for elem in cbest:
            let ng = resolv(g[0 .. ibest-1] & elem & g[ibest + 1 .. 80])
            if ng!="": return ng
        return ""
    else:
        return g

###############################################
# import strutils
# let gg = readFile("grids.txt").splitLines()[0..<1956]
# for g in gg:
#     echo resolv(g)

import std/rdstdin

var line: string
while true:
  let ok = readLineFromStdin("", line)
  if not ok: break # ctrl-C or ctrl-D will cause a break
  if line.len > 0: echo resolv(line)
