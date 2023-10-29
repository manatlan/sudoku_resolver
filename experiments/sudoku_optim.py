#! python3 -uOO
############################################### my resolver ;-) (backtracking)
sqr   = lambda g,x,y: g[y*9+x:y*9+x+3] + g[y*9+x+9:y*9+x+12] + g[y*9+x+18:y*9+x+21]
col   = lambda g,x:   g[x::9]
row   = lambda g,y:   g[y*9:y*9+9]
free  = lambda g,x,y: set("123456789") - set(col(g,x) + row(g,y) + sqr(g,(x//3)*3,(y//3)*3))

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
# the original algo + the 2e71828 optim (+20lines)
###############################################
def resolv(g):
    best = [None,set("123456789")]

    # find the hole where there is a minimal permutation
    for i in range(81):
        if g[i]==".":
            avails=free(g,i % 9, i // 9)
            if not avails:
                return None # not solvable
            else:
                if len(avails) < len(best[1]):
                    best = [i,avails]

                    if len(avails) == 1:
                        # Only one candidate here; we can't do better...
                        break

    if best[0] != None: 
        i,avails = best
        for c in avails:
            ng = resolv( g[:i] + c + g[i+1:] )
            if ng: return ng
    else: # no hole !
        return g  # Solved
###############################################
# def resolv(x):
#     # find the hole where there is a minimal permutation
#     print(x)
#     holes={i:free(x,i % 9, i // 9) for i in range(81)}
#     if not holes: 
#         return x
#     else:
#         d=sorted( holes.items() , key=lambda x: len(x[1]))
#         while d:
#             i,avails = d.pop(0)
#             i=i-1
#             for c in avails:
#                 ng = resolv( x[:i] + c + x[i+1:] )
#                 if ng: return ng
#             return None
import time

gg = [i.strip() for i in open("g_simples.txt")][:100]

t=time.monotonic()
for g in gg:
    rg=resolv(g)
    assert rg and rg.find(".")<0, "not resolved ?!"
    print(rg)

print( "Took: ", time.monotonic() - t , f"for {len(gg)} grids")