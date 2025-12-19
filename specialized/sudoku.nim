#!./make.py --10
#INFO: algo with specialized types using bitsets (optimized by copilot)

import std/[rdstdin, strutils]

# NumSet: represent 1-9 values using bits 0-8 in a uint16
type NumSet = uint16

const ALL_SET: NumSet = 0b1_1111_1111
const EMPTY_SET: NumSet = 0

func oneHot(val: uint8): NumSet =
    NumSet(1) shl int(val)

func popcount(x: NumSet): int =
    # Naive popcount for small sets
    var count = 0
    var bits = x
    while bits != 0:
        count += int(bits and 1)
        bits = bits shr 1
    count

func val(x: NumSet): uint8 =
    # Find the position of the lowest set bit
    for i in 0..<9:
        if (x and (NumSet(1) shl i)) != 0:
            return uint8(i)
    0

# Grid and solver
type Grid = object
    data: array[81, NumSet]
    spaces: seq[int]

proc parseGrid(s: string): Grid =
    var data: array[81, NumSet]
    var spaces: seq[int] = @[]
    
    for i, c in s:
        case c
        of '1'..'9':
            data[i] = oneHot(uint8(c) - uint8('1'))
        of '.':
            data[i] = EMPTY_SET
            spaces.add(i)
        else:
            discard
    
    Grid(data: data, spaces: spaces)

proc gridToString(g: Grid): string =
    var result = ""
    for x in g.data:
        if x == EMPTY_SET:
            result.add('.')
        else:
            result.add(char(uint8('1') + x.val()))
    result

proc sqr(g: Grid, x: int, y: int): NumSet =
    let x = (x div 3) * 3
    let y = (y div 3) * 3
    let i = y * 9 + x
    g.data[i] or g.data[i+1] or g.data[i+2] or
    g.data[i+9] or g.data[i+10] or g.data[i+11] or
    g.data[i+18] or g.data[i+19] or g.data[i+20]

proc col(g: Grid, x: int): NumSet =
    var result: NumSet = 0
    for y in 0..8:
        result = result or g.data[y*9 + x]
    result

proc row(g: Grid, y: int): NumSet =
    var result: NumSet = 0
    for x in 0..8:
        result = result or g.data[y*9 + x]
    result

proc free(g: Grid, x: int, y: int): NumSet =
    let col = col(g, x)
    let row = row(g, y)
    let sqr = sqr(g, x, y)
    ALL_SET and not (col or row or sqr)

proc resolv(g: var Grid, spaceIdx: int): bool =
    if spaceIdx >= g.spaces.len:
        return true
    
    var ibest = -1
    var cbest = ALL_SET
    var cbestLen = 10
    
    for idx in spaceIdx..<g.spaces.len:
        let i = g.spaces[idx]
        let c = free(g, i mod 9, i div 9)
        
        if c == EMPTY_SET:
            return false
        
        let clen = popcount(c)
        if clen < cbestLen:
            ibest = idx
            cbest = c
            cbestLen = clen
        
        if clen == 1:
            break
    
    if ibest >= 0:
        # Swap spaces[spaceIdx] with spaces[ibest]
        let temp = g.spaces[spaceIdx]
        g.spaces[spaceIdx] = g.spaces[ibest]
        g.spaces[ibest] = temp
        
        let s = g.spaces[spaceIdx]
        
        # Try each possibility
        var bit = cbest
        while bit != 0:
            let candidate = bit and (0 - bit) # isolate lowest set bit
            bit = bit xor candidate
            
            g.data[s] = candidate
            if resolv(g, spaceIdx + 1):
                return true
        
        g.data[s] = EMPTY_SET
        
        # Swap back
        let temp2 = g.spaces[spaceIdx]
        g.spaces[spaceIdx] = g.spaces[ibest]
        g.spaces[ibest] = temp2
        
        return false
    
    return true

###############################################
# Main loop

var line: string
while true:
    let ok = readLineFromStdin("", line)
    if not ok: break
    if line.len > 0:
        var grid = parseGrid(line)
        discard resolv(grid, 0)
        echo gridToString(grid) & " "
