from time import now

"""
this is a optimized/mojo version of the original one (--> 3.6s)
(the goal is to reach the speed of the C version, with mojo (without changing the algo!))
(but "dojo.mojo" has easily reached this goal (but not the same algo/structures!) !!!!)
"""
alias D16 = SIMD[DType.uint8, 16]   # ideal is 9, but should be a **2 .. so 16 !

fn sqr(g:String,x:Int,y:Int) -> D16:
    let off=y*9+x
    var xx=D16()
    @unroll
    for i in range(3):
        xx[i]=ord(g[off+i])
        xx[i+3]=ord(g[off+i+9])
        xx[i+6]=ord(g[off+i+18])
    return xx

fn col(g:String,x:Int) -> D16:
    var xx=D16()
    @unroll
    for i in range(9):
        xx[i]=ord(g[i*9+x])
    return xx

fn row(g:String,y:Int) -> D16:
    let off=y*9
    var xx=D16()
    @unroll
    for i in range(9):
        xx[i]=ord(g[off+i])
    return xx

fn indexOf(s:String,c:String) -> Int:
    for i in range(len(s)):
        if ord(s[i]) == ord(c):
            return i
    return -1

fn free(g:String,x:Int,y:Int) -> String:
    "Returns a string of numbers that can be fit at (x,y)."
    let _s = sqr(g,(x//3)*3,(y//3)*3)
    let _c = col(g,x)
    let _r = row(g,y)

    var avails=String()
    @unroll
    for c in range(49,49+9):
        if (not (_s==c).reduce_or()) and (not (_c==c).reduce_or()) and (not (_r==c).reduce_or()):
            # no C in row/col/sqr
            avails+= chr(c)[0]

    return avails

@always_inline
fn _mutate(g:String,idx:Int,c:String) -> String:
    "Mutate the grid, by replacing char at index 'idx' by the 'c' one."
    var tampon=String(".................................................................................")
    memcpy(tampon._as_ptr(),g._as_ptr(),81)
    memcpy(tampon._as_ptr()+idx,c._as_ptr(),1)
    return tampon
    # return g[:idx] + c[0] + g[idx+1:]


fn resolv(g: String) -> String:
    let i=indexOf(g,".")
    if i>=0:
        let x=free(g,i%9,i//9)
        for idx in range(len(x)):
            let ng=resolv( _mutate(g,i,x[idx]) )
            if ng: return ng
        return ""
    else:
        return g

fn main() raises:
    let buf = open("g_simples.txt", "r").read()
    let t=now()
    for i in range(100):
        # let ptr=StringRef( buf._as_ptr()+i*82,81)
        # let g=resolv(ptr)
        let g=resolv(buf[i*82:i*82+81])
        print(g)
    print("Took:",(now() - t)/1_000_000_000)
