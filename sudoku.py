#! python3 -uOO
############################################### my resolver ;-) (backtracking)
freeset  = lambda n:     set("123456789.") ^ set(n)
square   = lambda g,x,y: g[y*9+x:y*9+x+3] + g[y*9+x+9:y*9+x+12] + g[y*9+x+18:y*9+x+21]
interset = lambda g,x,y: freeset(g[x::9]) & freeset(g[y*9:y*9+9]) & freeset(square(g,(x//3)*3,(y//3)*3))

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
    assert rg and rg.rfind(".")<0, "not resolved ?!"
    echo(rg)

echo( "Took: ", getTime() - t )