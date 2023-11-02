from time import now

#INFO: the simple algo, with strings

fn sqr(g:String,x:Int,y:Int) -> String:
    return g[y*9+x:y*9+x+3] + g[y*9+x+9:y*9+x+12] + g[y*9+x+18:y*9+x+21]
fn col(g:String,x:Int) -> String:
    return g[x::9]
fn row(g:String,y:Int) -> String:
    return g[y*9:y*9+9]

fn freeset(n:String) -> String:
    # Set("123456789") - Set(n)
    let lx = StringRef("123456789")
    var ll = String("")
    for i in range(len(lx)):
        if indexOf(n,lx[i])<0:
            ll += lx[i]

    return ll

fn indexOf(s:String,c:String) -> Int:
    for i in range(len(s)):
        if s[i]==c:
            return i
    return -1

fn free(g:String,x:Int,y:Int) -> String:
    # interset = lambda g,x,y: freeset(vertiz(g,x)) & freeset(horiz(g,y)) & freeset(square(g,(x//3)*3,(y//3)*3))
    return freeset(col(g,x) + row(g,y) + sqr(g,(x//3)*3,(y//3)*3))

fn resolv(g: String) -> String:
    let i=indexOf(g,".")
    if i>=0:
        let x=free(g,i%9,i//9)
        for idx in range(len(x)):
            let ng=resolv( g[:i] + x[idx] + g[i+1:] )
            if ng: return ng
        return ""
    else:
        return g

fn main() raises:
    let buf = open("grids.txt", "r").read()
    let t=now()
    for i in range(100):
        let g=resolv(buf[i*82:i*82+81])
        if indexOf(g,".")>=0:
            print("error")
        else:
            print(g)
    print("Took:",(now() - t)/1_000_000_000,"s")
