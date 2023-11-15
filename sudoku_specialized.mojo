
#INFO: the simple algo, with specialized mojo-types

from time import now

alias GROUP = SIMD[DType.uint8, 16]   # reality is 9, but should be a **2 .. so 16 !

struct Grid:
    var data: Buffer[81, DType.uint8]

    fn __init__(inout self:Grid, g:String) -> None:
        "Create from a string (of 81 chars)."
        let dtp = DTypePointer[DType.uint8].alloc(81)
        self.data = Buffer[81, DType.uint8](dtp)
        
        @unroll
        for idx in range(81):
            self.data[idx] = ord(g[idx])-48 if g[idx]!="." else 0

    fn sqr(self:Grid,x:Int,y:Int) -> GROUP:
        let off=y*9+x
        var group=GROUP().splat(0)
        @unroll
        for i in range(3):
            group[i]=self.data[off+i]
            group[i+3]=self.data[off+i+9]
            group[i+6]=self.data[off+i+18]
        return group

    fn col(self:Grid,x:Int) -> GROUP:
        var group=GROUP().splat(0)
        @unroll
        for i in range(9):
            group[i]=self.data[i*9+x]
        return group

    fn row(self:Grid,y:Int) -> GROUP:
        let off=y*9
        var group=GROUP().splat(0)
        @unroll
        for i in range(9):
            group[i]=self.data[off+i]
        return group

    fn free(self: Grid, x: Int, y: Int) -> InlinedFixedVector[UInt8]:
        "Returns a string of numbers that can be fit at (x,y)."
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
        var i:Int = -1
        for x in range(81):
            if self.data[x]==0:
                i=x
                break

        if i>=0:
            let x=self.free(i%9,i//9)
            for idx in range(len(x)):
                self.data[i]=x[idx].__int__()
                if self.solve(): 
                    return True
            self.data[i]=0
            return False
        else:
            return True


    fn to_string(self:Grid) -> String:
        var str=String("")
        @unroll
        for i in range(81):
            let c = self.data[i].__int__()
            str+= chr(48+c)[0] if c else "."
        return str            

fn main() raises:
    let buf = open("grids.txt", "r").read()
    let t=now()
    for i in range(100):
        let g=Grid(buf[i*82:i*82+81])
        print( g.solve() and g.to_string() )
    print("Took:",(now() - t)/1_000_000_000,"s")
