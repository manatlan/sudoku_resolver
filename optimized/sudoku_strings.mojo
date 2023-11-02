from time import now
alias GROUP = SIMD[DType.uint8, 16]   # ideal is 9, but should be a **2 .. so 16 !

#INFO: optimized algo, with strings


fn sqr(g:String,x:Int,y:Int) -> GROUP:
    let off=y*9+x
    var group=GROUP().splat(0)
    @unroll
    for i in range(3):
        group[i]=ord(g[off+i])
        group[i+3]=ord(g[off+i+9])
        group[i+6]=ord(g[off+i+18])
    return group

fn col(g:String,x:Int) -> GROUP:
    var group=GROUP().splat(0)
    @unroll
    for i in range(9):
        group[i]=ord(g[i*9+x])
    return group

fn row(g:String,y:Int) -> GROUP:
    let off=y*9
    var group=GROUP().splat(0)
    @unroll
    for i in range(9):
        group[i]=ord(g[off+i])
    return group

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


fn indexOf(s:String,c:String) -> Int:
    for i in range(len(s)):
        if s[i]==c:
            return i
    return -1



fn resolv_old(g: String) -> String:
    let i=indexOf(g,".")
    if i>=0:
        let x=free(g,i%9,i//9)
        for idx in range(len(x)):
            let ng=resolv( g[:i] + x[idx] + g[i+1:] )
            if ng: return ng
        return ""
    else:
        return g

fn resolv(g: String) -> String:
    var ibest:Int=-1
    var cbest=String("123456789")
    
    for i in range(81):
        if g[i]==".":
            let avails=free(g,i%9,i//9)
            if not avails:
                return ""
            else:
                if len(avails) < len(cbest):
                    ibest=i
                    cbest=avails
                    
                    if len(avails)==1:
                        break
        
    if ibest != -1:
        for idx in range(len(cbest)):
            let ng=resolv( g[:ibest] + cbest[idx] + g[ibest+1:] )
            if ng: return ng
        return ""
    else:
        return g

fn main() raises:
    let buf = open("grids.txt", "r").read()
    let t=now()
    for i in range(1956):
        let g=resolv(buf[i*82:i*82+81])
        print(g)
    print("Took:",(now() - t)/1_000_000_000,"s")

