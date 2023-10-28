from time import now

"""
this is a optimized/mojo version of the original one
(the goal is to reach the speed of the C version, with mojo)
"""

fn sqr(g:String,x:Int,y:Int) -> String:
    return g[y*9+x:y*9+x+3] + g[y*9+x+9:y*9+x+12] + g[y*9+x+18:y*9+x+21]
fn col(g:String,x:Int) -> String:
    return g[x::9]
fn row(g:String,y:Int) -> String:
    return g[y*9:y*9+9]

fn indexOf(s:String,c:String) -> Int:
    for i in range(len(s)):
        if ord(s[i]) == ord(c):
            return i
    return -1

fn free(g:String,x:Int,y:Int) -> String:
    "Returns a string of numbers that can be fit at (x,y)."

    fn trans2simd(x:String) -> SIMD[DType.uint8, 16]:
        var xx=SIMD[DType.uint8, 16]()
        @unroll
        for i in range(9):
            xx[i]=ord(x[i])
        return xx

    let _s= trans2simd(sqr(g,(x//3)*3,(y//3)*3))
    let _c= trans2simd(col(g,x))
    let _r= trans2simd(row(g,y))

    var avails=String()
    @unroll
    for c in range(49,49+9):
        if (not (_s==c).reduce_or()) and (not (_c==c).reduce_or()) and (not (_r==c).reduce_or()):
            # no C in row/col/sqr
            avails+= chr(c)[0]

    return avails

fn _mutate(g:String,idx:Int,c:String) -> String:
    "Mutate the grid, by replacing char at index 'idx' by the 'c' one."
    # var tampon=String(".................................................................................")
    # memcpy(tampon._as_ptr(),g._as_ptr(),81)
    # memcpy(tampon._as_ptr()+idx,c._as_ptr(),1)
    # return tampon
    return g[:idx] + c[0] + g[idx+1:]


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
        let g=resolv(buf[i*82:i*82+81])
        if indexOf(g,".")>=0:
            print("error")
        else:
            print(g)
    print("Took:",(now() - t)/1_000_000_000)
