#!./make.py

#INFO: algo with strings

############################################### my resolver ;-) (backtracking)
sqr   = lambda g,x,y: g[y*9+x:y*9+x+3] + g[y*9+x+9:y*9+x+12] + g[y*9+x+18:y*9+x+21]
col   = lambda g,x:   g[x::9]
row   = lambda g,y:   g[y*9:y*9+9]
# free  = lambda g,x,y: set("123456789") - set(col(g,x) + row(g,y) + sqr(g,(x//3)*3,(y//3)*3))
def free(g:str,x:int,y:int) -> str:
    t27=col(g,x) + row(g,y) + sqr(g,(x//3)*3,(y//3)*3)
    freeset=""
    for c in "123456789":
        if c not in t27:
            freeset+=c
    return freeset
    
def resolv(g):
    ibest=-1
    cbest="123456789"
    for i in range(81):
        if g[i]==".":
            avails=free(g,i%9,i//9)
            if not avails:
                return ""
            else:
                if len(avails) < len(cbest):
                    ibest=i
                    cbest=avails
                    
                    if len(avails)==1:
                        break

    if ibest != -1:
        for c in cbest:
            ng = resolv( g[:ibest] + c + g[ibest+1:] )
            if ng: return ng
    else:
        return g
###############################################

import sys

for g in sys.stdin:
# for g in [i.strip() for i in open("grids.txt")]:
    print(resolv(g.strip()))

