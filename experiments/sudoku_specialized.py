#! python3 -uOO

#INFO: the simple algo, with specialized types (slower than the string version!)

############################################### my resolver ;-) (backtracking)

class Grid:
    def __init__(self, grid:str):
        self.rows=[]
        for y in range(9):
            row=[]
            for x in range(9):
                c=grid[y*9+x]
                row.append( 0 if c=="." else ord(c)-48 ) 
            self.rows.append(row)

    def row(self,y:int) -> set:
        'Returns a set of distinct values, of the row y.'
        return set( self.rows[y] )

    def col(self,x:int) -> set:
        'Returns a set of distinct values, of the column x.'
        return set( [self.rows[y][x] for y in range(9)] )

    def sqr(self,x:int,y:int) -> set:
        'Returns a set of distinct values, in the square at x,y.'
        return set( self.rows[y][x:x+3] + self.rows[y+1][x:x+3] + self.rows[y+2][x:x+3] )

    def free(self,x,y):
        "Returns a list of available values that can be fit in (x,y)."
        avails = {1,2,3,4,5,6,7,8,9}
        avails-=self.col(x)
        avails-=self.row(y)
        avails-=self.sqr((x//3)*3,(y//3)*3)
        return avails

    def __str__(self):
        return "".join( [ "".join( ["." if x==0 else chr(x+48) for x in row]) for row in self.rows] )

    def solve(self) -> bool:
        for y in range(9):
            for x in range(9):
                if not self.rows[y][x]:
                    for c in self.free(x,y):
                        self.rows[y][x]=c
                        if self.solve():
                            return True
                    self.rows[y][x]=0
                    return False
        return True
###############################################

import time

gg = [Grid(i.strip()) for i in open("grids.txt")][:100]

t=time.monotonic()
for g in gg:
    print(g.solve() and g)
print( "Took: ", time.monotonic() - t)