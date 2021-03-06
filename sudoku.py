#! python3 -uOO
############################################### my resolver ;-) (backtracking)
square   = lambda g,x,y: g[y*9+x:y*9+x+3] + g[y*9+x+9:y*9+x+12] + g[y*9+x+18:y*9+x+21]
vertiz   = lambda g,x:   g[x::9]
horiz    = lambda g,y:   g[y*9:y*9+9]
freeset  = lambda n:     set("123456789") - set(n)
interset = lambda g,x,y: freeset(vertiz(g,x)) & freeset(horiz(g,y)) & freeset(square(g,(x//3)*3,(y//3)*3))

def resolv(g):
    i=g.find(".")
    if i>=0:
        for elem in interset(g,i%9,i//9):
            ng=resolv( g[:i] + elem + g[i+1:] )
            if ng: return ng
    else:
        return g
###############################################

import datetime
getTime=lambda: datetime.datetime.now()
def echo(*a): print(" ".join([str(i) for i in a]))

gg = [i.strip() for i in open("g_simples.txt")][:100]

t=getTime()
for g in gg:
    rg=resolv(g)
    assert rg and rg.find(".")<0, "not resolved ?!"
    echo(rg)

echo( "Took: ", getTime() - t )