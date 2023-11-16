#!./make.py
from tensor import Tensor
from time import now

#INFO: the optimizes algo, with Tensor (100grids)


struct Grid[dtype: DType = DType.uint8, dim: Int = 9]():
  var mat: Tensor[dtype]

  alias GROUP = SIMD[dtype, 16]   # reality is 9, but should be a **2 .. so 16 !

  fn __init__(inout self, grid:String):
    self.mat = Tensor[dtype](self.dim,self.dim)
    for i in range(len(grid)):
        let c=grid[i]
        self.mat.__setitem__(i,0 if c=="." else ord(grid[i])-48)

  #-------------------------------------------------------
  fn row(self,y:Int) -> self.GROUP:
    var group=self.GROUP().splat(0)
    @unroll
    for x in range(9):
        group[x] = self.mat[x,y]
    return group

  fn col(self,x:Int) -> self.GROUP:
    var group=self.GROUP().splat(0)
    @unroll
    for y in range(9):
        group[y] = self.mat[x,y]
    return group

  fn sqr(self,x:Int,y:Int) -> self.GROUP:
    var group=self.GROUP().splat(0)
    @unroll
    for i in range(3):
        group[i]=self.mat[x+i,y]
        group[i+3]=self.mat[x+i,y+1]
        group[i+6]=self.mat[x+i,y+2]
    return group

  fn free(self, x: Int, y: Int) -> InlinedFixedVector[SIMD[dtype,1]]:
    "Returns a string of numbers that can be fit at (x,y)."
    let _s = self.sqr((x // 3) * 3, (y // 3) * 3)
    let _c = self.col(x)
    let _r = self.row(y)

    var avails = InlinedFixedVector[SIMD[dtype,1]](9)

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
  #-------------------------------------------------------



#   fn solve(inout self) -> Bool:
#     for x in range(9):
#         for y in range(9):
#             if self[x,y]==0:
#                 let ll=self.free(x,y)
#                 for idx in range(len(ll)):
#                     self[x,y] = ll[idx]
#                     if self.solve(): 
#                         return True
#                 self[x,y] = 0
#                 return False
#     return True


  fn solve(inout self) -> Bool:
    var xbest:Int=-1
    var ybest:Int=-1
    var cbest=InlinedFixedVector[SIMD[dtype,1]](9)
    @unroll
    for i in range(1,10):
        cbest.append(i)

    # searching a hole, with minimal choices (1 is better)    
    @unroll
    for x in range(9):
        for y in range(9):
            if self[x,y]==0:
                let avails=self.free(x,y)
                if len(avails)==0:
                    return False
                else:
                    if len(avails) < len(cbest):
                        xbest=x
                        ybest=y
                        cbest=avails
                        
                        if len(avails)==1:  # can't find better
                            break

    if xbest != -1:
        for idx in range(len(cbest)):
            self[xbest,ybest] = cbest[idx]
            if self.solve(): 
                return True
        self[xbest,ybest] = 0
        return False
    else:
        return True


  fn print(self):
    print(self.mat)

#   fn to_string(self) -> String:
#     var g=String("")
#     for x in range(9):
#         for y in range(9):
#             let c=self[x,y]
#             g+=chr(c.__int__()+48) if c else "."
                
#     return g

  fn __getitem__(self,x:Int,y:Int)->SIMD[dtype,1]:
    return self.mat[x,y]
  fn __setitem__(inout self,x:Int,y:Int,v:SIMD[dtype,1]):
    self.mat.__setitem__(x*9+y,v)

fn main() raises:
    let buf = open("grids.txt", "r").read()
    let t=now()
    for i in range(100):
        var g=Grid(buf[i*82:i*82+81])
        g.solve()
    print("Took:",(now() - t)/1_000_000_000,"s")
