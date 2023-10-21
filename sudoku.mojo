
fn square(g:String,x:Int,y:Int) -> String:
    return g[y*9+x:y*9+x+3] + g[y*9+x+9:y*9+x+12] + g[y*9+x+18:y*9+x+21]
fn vertiz(g:String,x:Int) -> String:
    return g[x::9]
fn horiz(g:String,y:Int) -> String:
    return g[y*9:y*9+9]

fn freeset(n:String) -> String:
    # Set("123456789") - Set(n)
    var lx:String="123456789"
    for i in range(len(n)):
        if n[i]!=".":
            try:
                # replace digit by a space
                let pos=atol( n[i] )
                lx= lx[:pos-1]+" "+lx[pos:]
            except:
                pass

    # remove empty spaces in string
    var ll:String=""
    for i in range(len(lx)):
        if lx[i]!=" ":
            ll=ll + lx[i]
    return ll

fn indexOf(g:String,c:String) -> Int:
    for i in range(len(g)):
        if g[i]==c:
            return i
    return -1

fn interset(g:String,x:Int,y:Int) -> String:
    # interset = lambda g,x,y: freeset(vertiz(g,x)) & freeset(horiz(g,y)) & freeset(square(g,(x//3)*3,(y//3)*3))
    let v=freeset(vertiz(g,x))
    let h=freeset(horiz(g,y))
    let s=freeset(square(g,(x//3)*3,(y//3)*3))

    var r:String=""
    for i in range(len(v)):
        let c=v[i]
        if indexOf(h,c)>=0 and indexOf(s,c)>=0:
            r=r+c
    return r

fn resolv(g: String) -> String:
    let i=indexOf(g,".")
    if i>=0:
        let x=interset(g,i%9,i//9)
        for idx in range(len(x)):
            let ng=resolv( g[:i] + x[idx] + g[i+1:] )
            if ng: return ng
    else:
        return g
    return ""

from time import now

fn main():
    try:
        var  f = open("g_simples.txt", "r")
        let buf=f.read()
        let t=now()
        for i in range(100):
            var g=buf[i*82:i*82+81]
            g=resolv(g)
            if indexOf(g,".")>=0:
                print("error")
            else:
                print(g)
        print("Took:",(now() - t)/1_000_000_000)
        f.close()
    except:
        pass
