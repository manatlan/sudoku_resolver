from python import Python

@value
struct Pair:
    var x: Int
    var y: Int

    # fn __init__(inout self: Pair, x: Int, y: Int):
    #     self.x = x
    #     self.y = y

    # fn __str__(inout self) -> String:
    #     return "hhh"

def main():
    let py = Python.import_module("sys")

    print( py.path )

    let p=Pair(12,4)
    print(p.x)
