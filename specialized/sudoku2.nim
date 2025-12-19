#!./make.py --10
#INFO: from c to nim (by gemini3)
import strutils, bitops, std/syncio

type
  Sudoku = array[81, char]
  Masks = array[9, uint16]

var
  rowMask, colMask, boxMask: Masks

proc getBox(row, col: int): int {.inline.} =
  (row div 3) * 3 + (col div 3)

proc initMasks(g: Sudoku) =
  for i in 0..<9:
    rowMask[i] = 0
    colMask[i] = 0
    boxMask[i] = 0
  
  for i in 0..<81:
    if g[i] != '.':
      let bit = 1.uint16 shl (ord(g[i]) - ord('1'))
      let row = i div 9
      let col = i mod 9
      rowMask[row] = rowMask[row] or bit
      colMask[col] = colMask[col] or bit
      boxMask[getBox(row, col)] = boxMask[getBox(row, col)] or bit

proc getCandidates(idx: int): uint16 {.inline.} =
  let row = idx div 9
  let col = idx mod 9
  return 0x1FF.uint16 and not (rowMask[row] or colMask[col] or boxMask[getBox(row, col)])

proc place(idx: int, val: char) {.inline.} =
  let bit = 1.uint16 shl (ord(val) - ord('1'))
  let row = idx div 9
  let col = idx mod 9
  rowMask[row] = rowMask[row] or bit
  colMask[col] = colMask[col] or bit
  boxMask[getBox(row, col)] = boxMask[getBox(row, col)] or bit

proc propagate(g: var Sudoku): bool =
  var changed = true
  var iterations = 0
  
  while changed and iterations < 15:
    changed = false
    iterations.inc
    
    # 1. Naked Singles
    for i in 0..<81:
      if g[i] == '.':
        let cand = getCandidates(i)
        if cand == 0: return false
        if countSetBits(cand) == 1:
          # Correction ici : utilisation de countTrailingZeroBits
          let digitIdx = countTrailingZeroBits(cand)
          g[i] = chr(ord('1') + digitIdx)
          place(i, g[i])
          changed = true

    # 2. Hidden Singles (Lignes)
    for row in 0..<9:
      for digit in 0..<9:
        let bit = 1.uint16 shl digit
        if (rowMask[row] and bit) != 0: continue
        var count = 0
        var lastCol = -1
        for col in 0..<9:
          let idx = row * 9 + col
          if g[idx] == '.' and (getCandidates(idx) and bit) != 0:
            count.inc
            lastCol = col
            if count > 1: break
        if count == 1:
          let idx = row * 9 + lastCol
          g[idx] = chr(ord('1') + digit)
          place(idx, g[idx])
          changed = true

    # 3. Hidden Singles (Colonnes)
    for col in 0..<9:
      for digit in 0..<9:
        let bit = 1.uint16 shl digit
        if (colMask[col] and bit) != 0: continue
        var count = 0
        var lastRow = -1
        for row in 0..<9:
          let idx = row * 9 + col
          if g[idx] == '.' and (getCandidates(idx) and bit) != 0:
            count.inc
            lastRow = row
            if count > 1: break
        if count == 1:
          let idx = lastRow * 9 + col
          g[idx] = chr(ord('1') + digit)
          place(idx, g[idx])
          changed = true
  
  return true

proc solve(g: var Sudoku): bool =
  if not propagate(g): return false

  var bestIdx = -1
  var minCount = 10
  var bestMask: uint16 = 0

  for i in 0..<81:
    if g[i] == '.':
      let cand = getCandidates(i)
      if cand == 0: return false
      let cnt = countSetBits(cand)
      if cnt < minCount:
        minCount = cnt
        bestIdx = i
        bestMask = cand
        if cnt == 1: break

  if bestIdx == -1: return true

  # Sauvegarde par valeur (très rapide en Nim)
  let backupG = g
  let backupRow = rowMask
  let backupCol = colMask
  let backupBox = boxMask

  for digit in 0..<9:
    if (bestMask and (1.uint16 shl digit)) != 0:
      g[bestIdx] = chr(ord('1') + digit)
      place(bestIdx, g[bestIdx])
      
      if solve(g): return true
      
      # Restauration
      g = backupG
      rowMask = backupRow
      colMask = backupCol
      boxMask = backupBox
  
  return false

proc main() =
  var line: string
  while stdin.readLine(line):
    let trimmed = line.strip()
    if trimmed.len >= 81:
      var grid: Sudoku
      for i in 0..<81: grid[i] = trimmed[i]
      initMasks(grid)
      if solve(grid):
        var res = newStringOfCap(81)
        for c in grid: res.add(c)
        echo res
      else:
        echo "No solution"

main()