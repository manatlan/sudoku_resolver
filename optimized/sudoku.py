#!./make.py

#INFO: the optimized algo, with strings (1956grids)

############################################### my resolver ;-) (backtracking)
sqr   = lambda g,x,y: g[y*9+x:y*9+x+3] + g[y*9+x+9:y*9+x+12] + g[y*9+x+18:y*9+x+21]
col   = lambda g,x:   g[x::9]
row   = lambda g,y:   g[y*9:y*9+9]
# free  = lambda g,x,y: set("123456789") - set(col(g,x) + row(g,y) + sqr(g,(x//3)*3,(y//3)*3))
def free(g,x,y):
    t27=col(g,x) + row(g,y) + sqr(g,(x//3)*3,(y//3)*3)
    return "".join([c for c in "123456789" if c not in t27])

###############################################
# the original algo
###############################################
# def resolv(g):
#     i=g.find(".")
#     if i>=0:
#         for elem in ffree(g,i%9,i//9):
#             ng=resolv( g[:i] + elem + g[i+1:] )
#             if ng: return ng
#     else:
#         return g

###############################################
# the original algo + optim (+5lines)
###############################################
def resolv(g):
    holes={}
    for i in range(81):
        if g[i]==".":
            holes[i]=free(g,i % 9, i // 9)
            if len(holes[i])==1: break
    if len(holes)>0: 
        i,avails = sorted( holes.items() , key=lambda x: len(x[1])).pop(0)
        for c in avails:
            ng = resolv( g[:i] + c + g[i+1:] )
            if ng: return ng
    else:
        return g
###############################################

for g in [i.strip() for i in open("grids.txt")]:
    print(resolv(g))

