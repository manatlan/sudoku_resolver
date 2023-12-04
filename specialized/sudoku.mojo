#!./make.py --10

#INFO: algo with specialized types (use python to read stdin)
from utils.vector import InlinedFixedVector

alias GROUP = SIMD[DType.uint8, 16]   # reality is 9, but should be a **2 .. so 16 !

struct Grid(Stringable):
    var data: Buffer[81, DType.uint8]

    fn __init__(inout self:Grid, g:String) -> None:
        "Create from a string (of 81 chars)."
        let dtp = DTypePointer[DType.uint8].alloc(81)
        self.data = Buffer[81, DType.uint8](dtp)
        
        @unroll
        for idx in range(81):
            self.data[idx] = ord(g[idx])-48 if g[idx]!="." else 0

    fn sqr(self:Grid,x:Int,y:Int) -> GROUP:
        'Returns a group of 9 values, of the square at x,y.'
        let off=y*9+x
        var group=GROUP().splat(0)
        @unroll
        for i in range(3):
            group[i]=self.data[off+i]
            group[i+3]=self.data[off+i+9]
            group[i+6]=self.data[off+i+18]
        return group

    fn col(self:Grid,x:Int) -> GROUP:
        'Returns a group of 9 values, of the column x.'
        var group=GROUP().splat(0)
        @unroll
        for i in range(9):
            group[i]=self.data[i*9+x]
        return group

    fn row(self:Grid,y:Int) -> GROUP:
        'Returns a group of 9 values, of the row y.'
        let off=y*9
        var group=GROUP().splat(0)
        @unroll
        for i in range(9):
            group[i]=self.data[off+i]
        return group

    fn free(self: Grid, x: Int, y: Int) -> InlinedFixedVector[UInt8]:
        "Returns a list of available values that can be fit in (x,y)."
        "(this thing is a bit tricky coz it uses simd operation, to be as fast as possible)"
        let _s = self.sqr((x // 3) * 3, (y // 3) * 3)
        let _c = self.col(x)
        let _r = self.row(y)

        var avails = InlinedFixedVector[UInt8](9)

        @unroll
        for c in range(1, 10):
            if (
                (not (_s == c).reduce_or())
                and (not (_c == c).reduce_or())
                and (not (_r == c).reduce_or())
            ):
                # no C in row/col/sqr
                avails.append(c)
        return avails

    fn solve(self: Grid) -> Bool:
        "Solve the grid, returns true/false if it cans."
        "It's the optimized algo : so it will try the hole which have a minimal choice (ideally 1)."
        var ibest:Int=-1
        var cbest=InlinedFixedVector[UInt8](9)
        @unroll
        for i in range(1,10):
            cbest.append(i)
        
        for i in range(81):
            if self.data[i]==0:
                let avails=self.free(i%9,i//9)
                if len(avails)==0:
                    return False
                else:
                    if len(avails) < len(cbest):
                        ibest=i
                        cbest=avails
                        
                        if len(avails)==1:
                            break
            
        if ibest != -1:
            for idx in range(len(cbest)):
                self.data[ibest]=cbest[idx].__int__()
                if self.solve(): return True
            self.data[ibest]=0
            return False
        else:
            return True

    fn __str__(self:Grid) -> String:
        "Returns a string of 81chars of the grid."
        var str=String("")
        @unroll
        for i in range(81):
            let c = self.data[i].__int__()
            str+= chr(48+c)[0] if c else "."
        return str           

# fn main() raises:
#     let buf = open("grids.txt", "r").read()
#     for i in range(1956):
#         let g=Grid(buf[i*82:i*82+81])
#         print( g.solve() and g.to_string() )

from python import Python
def main():
    let sys = Python.import_module("sys")
    var py = Python()
    for line in sys.stdin:
        let g=Grid(py.__str__(line))
        if g.solve():
            print( g )
