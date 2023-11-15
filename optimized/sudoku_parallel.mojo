from time import now
from math import iota
from algorithm import parallelize

#INFO: optimized algo, with specialized types & parallelization

alias GROUP = SIMD[DType.uint8, 16]   # reality is 9, but should be a **2 .. so 16 !

@value
struct Grid:
    var data: Buffer[81, DType.uint8]

    fn __init__(inout self:Grid, g:String) -> None:
        "Create from a string (of 81 chars)."
        let dtp = DTypePointer[DType.uint8].alloc(81)
        self.data = Buffer[81, DType.uint8](dtp)
        let ptr = g._buffer.data.bitcast[UInt8]()
        @unroll
        for idx in range(81):
            self.data[idx] = ptr[idx]-48 if ptr[idx]!=46 else 0
        _=g

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

    fn free(self:Grid,x:Int,y:Int) -> InlinedFixedVector[UInt8]:
        "Returns a string of numbers that can be fit at (x,y)."
        let _s = self.sqr((x//3)*3,(y//3)*3)
        let _c = self.col(x)
        let _r = self.row(y)

        var avails = InlinedFixedVector[UInt8](9)
        @unroll
        for c in range(1,10):
            if (not (_s==c).reduce_or()) and (not (_c==c).reduce_or()) and (not (_r==c).reduce_or()):
                # no C in row/col/sqr
                avails.append( c )

        return avails

    
    fn solve(self:Grid) -> Bool:
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

    fn to_string(self:Grid) -> String:
        var str=String("")
        @unroll
        for i in range(81):
            let c = self.data[i].__int__()
            str+= chr(48+c)[0] if c else "."
        return str 

alias workers = 4

fn main() raises:
    let buf = open("grids.txt", "r").read()
    let t=now()

    @parameter
    fn in_p(i:Int):
        let g=Grid(buf[i*82:i*82+81])
        print( g.solve() and g.to_string() )

    parallelize[in_p](1956,workers)
    print("Took:",(now() - t)/1_000_000_000,"s")
    
    _=buf^ #extend lifetime of pointer
