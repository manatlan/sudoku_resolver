#!./make.py --codon

#INFO: the simple|optimized algo, with specialized types (slower than the strings version!) (100grids)

"""
this version is more explicit, bicoz you can understand the diff between simple vs optimized
and the GridDataXXXX is the implemented specialized type

btw the implem with specilized type is slower than the string version (all python implem !!!) ;-)
"""

############################################### my resolver ;-) (backtracking)
from typing import List,Tuple,Set


class GridDataList:
    _rows: List[List[int]]
    def __init__(self, grid:str):
        self._rows = []
        for y in range(9):
            row=[]
            for x in range(9):
                c=grid[y*9+x]
                row.append( 0 if c=="." else ord(c)-48 ) 
            self._rows.append(row)

    def _row(self,y:int) ->  Set[int]:
        'Returns a set of distinct values, of the row y.'
        return set( self._rows[y] )

    def _col(self,x:int) ->  Set[int]:
        'Returns a set of distinct values, of the column x.'
        return set( [self._rows[y][x] for y in range(9)] )

    def _sqr(self,x:int,y:int) ->  Set[int]:
        'Returns a set of distinct values, in the square at x,y.'
        return set( self._rows[y][x:x+3] + self._rows[y+1][x:x+3] + self._rows[y+2][x:x+3] )

    def free(self,x,y) -> Set[int]:
        "Returns a list of available values that can be fit in (x,y)."
        avails = {1,2,3,4,5,6,7,8,9}
        avails-=self._col(x)
        avails-=self._row(y)
        avails-=self._sqr((x//3)*3,(y//3)*3)
        return avails

    def __str__(self) -> str:
        return "".join( [ "".join( ["." if x==0 else chr(x+48) for x in row]) for row in self._rows] )

    def get(self,x:int,y:int) -> int:
        return self._rows[y][x]

    def set(self,x:int,y:int,c:int) -> int:
        self._rows[y][x]=c


class GridDataString:
    data: str
    def __init__(self, grid:str):
        self.data=grid

    def _row(self,y:int) -> str:
        return self.data[y*9:y*9+9]

    def _col(self,x:int) -> str:
        return self.data[x::9]

    def _sqr(self,x:int,y:int) -> str:
        return self.data[y*9+x:y*9+x+3] + self.data[y*9+x+9:y*9+x+12] + self.data[y*9+x+18:y*9+x+21]

    def free(self,x:int,y:int) -> set:
        avails = set("123456789") - set(self._col(x) + self._row(y) + self._sqr((x//3)*3,(y//3)*3))
        return set([ord(i)-48 for i in avails])

    def __str__(self) -> str:
        return self.data

    def get(self,x:int,y:int) -> int:
        c=self.data[y*9+x]
        return 0 if c=="." else ord(c)-48

    def set(self,x:int,y:int,v:int) -> int:
        i=y*9+x
        c=chr(v+48) if v>0 else "0"
        self.data = self.data[:i] + c + self.data[i+1:]


class Sudoku:
    grid:GridDataList

    def __init__(self, grid:GridDataList):
        self.grid=grid

    def find_hole(self) -> Tuple[int,int,Set[int]]:
        """the simple algo"""
        for y in range(9):
            for x in range(9):
                if not self.grid.get(x,y):
                    return (x,y,self.grid.free(x,y))
        return (-1,-1,set())

    def find_best_hole(self) -> Tuple[int,int,Set[int]]:
        """the optimized algo (return the hole with a minimal choices (ideally 1))"""
        xbest,ybest=-1,-1
        cbest={1,2,3,4,5,6,7,8,9}
        for y in range(9):
            for x in range(9):
                if not self.grid.get(x,y):
                    avails=self.grid.free(x,y)

                    if len(avails) < len(cbest):
                        xbest,ybest = x,y
                        cbest=avails
                        
                        if len(avails)==1:
                            break
        
        return (xbest,ybest,cbest)

    def solve(self,optimized=False) -> bool:
        if optimized:
            x,y,avails=self.find_best_hole()     # <- the optimized algo
        else:
            x,y,avails=self.find_hole()          # <- the simple algo
        
        if x>=0:
            for c in avails:
                self.grid.set(x,y,c)
                if self.solve():
                    return True
            self.grid.set(x,y,0)
            return False
        return True


###############################################

gg = [GridDataList(i.strip()) for i in open("grids.txt")][:100]

for g in gg:
    a=Sudoku(g)
    a.solve(optimized=True)
    print(g)
