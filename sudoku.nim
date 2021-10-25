#! nim c -d:danger -r

############################################### my resolver ;-) (backtracking)
proc square(g: string,x:int,y:int): string =
    let x=int(x/3)*3
    let y=int(y/3)*3
    g[y*9+x .. y*9+x+2] & g[y*9+x+9 .. y*9+x+11] & g[y*9+x+18 .. y*9+x+20]

proc horiz(g: string, y:int): string =
    var ligne: int = y * 9
    g[0+ligne .. 8+ligne]

proc vertiz(g: string, x:int): string =
    result = ""
    for y in 0 .. 8:
        var ligne: int = y * 9
        result.add g[x+ligne]

proc freeset(sg: string): set[char] =
  var s: set[char] = {}
  for c in sg: s.incl c
  {'1'..'9', '.'} - s


proc interset(g:string,x:int,y:int): set[char] =
    freeset(horiz(g,y)) * freeset(vertiz(g,x)) * freeset(square(g,x,y))

proc replace(g:string, pos:int, car: char): string = g[0..pos-1] & car & g[pos+1..80]

proc resolv(g:string): string =
    let i = g.find('.')
    if i>=0:
        for elem in interset(g,i mod 9,int(i/9)):
            let ng= resolv( replace(g,i,elem) )
            if ng != "": return ng
        return ""
    else:
        return g
###############################################

import strutils
import times

proc aff(g: string): void =
    echo ""
    for y in 0 .. 8:
        var t=join( horiz(g, y) ," ")
        echo t[0..5],"|",t[5..11],"|",t[11..16]
        if y<8 and (y+1) mod 3 == 0:
            echo "------+-------+------"

var gg= readFile("g_simples.txt").splitLines()[0..100]

let t = getTime()
for g in gg:
    let rg=resolv(g)
    assert rg!="" and rg.find(".")<0, "not resolved ?!"
    echo rg
echo "Took: ", getTime() - t

