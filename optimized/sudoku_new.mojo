from time import now

alias D16 = SIMD[DType.uint8, 16]   # ideal is 9, but should be a **2 .. so 16 !
alias GRID = DynamicVector[UInt8]
from memory.buffer import Buffer

@value
struct Grid:
    var data: Buffer[81, DType.uint8]
    var dtp: DTypePointer[DType.uint8]

    fn __init__(inout self:Grid, g:String) -> None:
        self.dtp = DTypePointer[DType.uint8].alloc(81)
        self.data = Buffer[81, DType.uint8](self.dtp)
        @unroll
        for idx in range(81):
            if g[idx]!=".":
                self.data[idx]=ord(g[idx])-48
            else:
                self.data[idx]=0

    fn __init__(inout self, g:Buffer[81, DType.uint8], idx:Int,c:Int) -> None:
        self.dtp = DTypePointer[DType.uint8].alloc(81)
        self.data = Buffer[81, DType.uint8](self.dtp)
        @unroll
        for i in range(81):
            self.data[i] = g[i]
        self.data[idx]=c

    fn __init__(inout self:Grid) -> None:
        self.dtp = DTypePointer[DType.uint8].alloc(1)
        self.data = Buffer[81, DType.uint8](self.dtp)
        self.data[0]=-1

    fn is_valid(self:Grid) -> Bool:
        return self.data[0]!=-1

    fn sqr(self:Grid,x:Int,y:Int) -> D16:
        let off=y*9+x
        var xx=D16()
        xx=xx.splat(0)
        @unroll
        for i in range(3):
            xx[i]=ord(self.data[off+i])
            xx[i+3]=ord(self.data[off+i+9])
            xx[i+6]=ord(self.data[off+i+18])
        return xx

    fn col(self:Grid,x:Int) -> D16:
        var xx=D16()
        xx=xx.splat(0)
        @unroll
        for i in range(9):
            xx[i]=ord(self.data[i*9+x])
        return xx

    fn row(self:Grid,y:Int) -> D16:
        let off=y*9
        var xx=D16()
        xx=xx.splat(0)
        @unroll
        for i in range(9):
            xx[i]=ord(self.data[off+i])
        return xx

    fn free(self:Grid,x:Int,y:Int) -> String:
        "Returns a string of numbers that can be fit at (x,y)."
        let _s = self.sqr((x//3)*3,(y//3)*3)
        let _c = self.col(x)
        let _r = self.row(y)

        var avails=String()
        @unroll
        for c in range(49,49+9):
            if (not (_s==c).reduce_or()) and (not (_c==c).reduce_or()) and (not (_r==c).reduce_or()):
                # no C in row/col/sqr
                avails+= chr(c)[0]
        return avails

    fn resolv(self:Grid) -> Grid:
        var ibest:Int=-1
        var cbest=String("123456789")
        
        for i in range(81):
            if self.data[i]==0:
                let avails=self.free(i%9,i//9)
                if not avails:
                    return Grid()   # bad
                else:
                    if len(avails) < len(cbest):
                        ibest=i
                        cbest=avails
                        
                        if len(avails)==1:
                            break
            
        if ibest != -1:
            for idx in range(len(cbest)):
                let ng=Grid( self.data, ibest, ord(cbest[idx])-48).resolv()
                if ng.is_valid(): return ng
            return Grid() # bad
        else:
            return self

    fn to_string(self:Grid) -> String:
        var ll=String("")
        for i in range(9*9):
            let c:Int = self.data[i].__int__()
            if c==0:
                ll+="."
            else:
                ll+=chr(48+c)[0]
        return ll            

fn main() raises:
    let buf = open("g_simples.txt", "r").read()
    let t=now()
    for i in range(1011):
        let g1=Grid(buf[i*82:i*82+81])
        # print(g1.to_string())
        print( g1.resolv().to_string() )
        # break
    print("Took:",(now() - t)/1_000_000_000,"sec")
