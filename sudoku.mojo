#!./make.py 
#INFO: algo with strings (use python to read stdin)

alias ALL = StringRef("123456789")

fn sqr(g:String,x:Int,y:Int) -> String:
    return g[y*9+x:y*9+x+3] + g[y*9+x+9:y*9+x+12] + g[y*9+x+18:y*9+x+21]
fn col(g:String,x:Int) -> String:
    return g[x::9]
fn row(g:String,y:Int) -> String:
    return g[y*9:y*9+9]

fn free(g:String,x:Int,y:Int) -> String:
    var t27=col(g,x) + row(g,y) + sqr(g,(x//3)*3,(y//3)*3)
    var freeset = String("")
    for i in range(len(ALL)):
        if t27.find(ALL[i])<0:
            freeset += ALL[i]
    return freeset

fn resolv(g: String) -> String:
    var ibest:Int=-1
    var cbest=String("123456789")
    
    for i in range(81):
        if g[i]==".":
            var avails=free(g,i%9,i//9)
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
            var ng=resolv( g[:ibest] + cbest[idx] + g[ibest+1:] )
            if ng: return ng
        return ""
    else:
        return g

# fn main() raises:
#     let buf = open("grids.txt", "r").read()
#     for i in range(50):
#         print( resolv(buf[i*82:i*82+81]) )

from python import Python
def main():
    var sys = Python.import_module("sys")
    var py = Python()
    for g in sys.stdin:
        print(resolv(py.__str__(g)))

