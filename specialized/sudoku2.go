package main
//INFO: from c to go (by gemini3)
import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
)

type Sudoku [81]byte
type Masks [9]uint16

type Solver struct {
	rowMask Masks
	colMask Masks
	boxMask Masks
}

func (s *Solver) initMasks(g *Sudoku) {
	for i := 0; i < 9; i++ {
		s.rowMask[i], s.colMask[i], s.boxMask[i] = 0, 0, 0
	}
	for i := 0; i < 81; i++ {
		if g[i] != '.' {
			bit := uint16(1) << (g[i] - '1')
			row, col := i/9, i%9
			s.rowMask[row] |= bit
			s.colMask[col] |= bit
			s.boxMask[(row/3)*3+(col/3)] |= bit
		}
	}
}

func (s *Solver) getCandidates(idx int) uint16 {
	row, col := idx/9, idx%9
	return 0x1FF & ^(s.rowMask[row] | s.colMask[col] | s.boxMask[(row/3)*3+(col/3)])
}

func (s *Solver) place(idx int, val byte) {
	bit := uint16(1) << (val - '1')
	row, col := idx/9, idx%9
	s.rowMask[row] |= bit
	s.colMask[col] |= bit
	s.boxMask[(row/3)*3+(col/3)] |= bit
}

func (s *Solver) propagate(g *Sudoku) bool {
	changed := true
	for iterations := 0; changed && iterations < 15; iterations++ {
		changed = false
		// 1. Naked Singles
		for i := 0; i < 81; i++ {
			if g[i] == '.' {
				cand := s.getCandidates(i)
				if cand == 0 { return false }
				if bits.OnesCount16(cand) == 1 {
					digitIdx := bits.TrailingZeros16(cand)
					g[i] = byte('1' + digitIdx)
					s.place(i, g[i])
					changed = true
				}
			}
		}
		// 2. Hidden Singles (Lignes)
		for row := 0; row < 9; row++ {
			for digit := uint16(0); digit < 9; digit++ {
				bit := uint16(1) << digit
				if (s.rowMask[row] & bit) != 0 { continue }
				count, lastCol := 0, -1
				for col := 0; col < 9; col++ {
					idx := row*9 + col
					if g[idx] == '.' && (s.getCandidates(idx)&bit) != 0 {
						count++
						lastCol = col
						if count > 1 { break }
					}
				}
				if count == 1 {
					idx := row*9 + lastCol
					g[idx] = byte('1' + digit)
					s.place(idx, g[idx])
					changed = true
				}
			}
		}
	}
	return true
}

func (s *Solver) solve(g *Sudoku) bool {
	if !s.propagate(g) { return false }

	bestIdx, minCount, bestMask := -1, 10, uint16(0)
	for i := 0; i < 81; i++ {
		if g[i] == '.' {
			cand := s.getCandidates(i)
			if cand == 0 { return false }
			cnt := bits.OnesCount16(cand)
			if cnt < minCount {
				minCount, bestIdx, bestMask = cnt, i, cand
				if cnt == 1 { break }
			}
		}
	}

	if bestIdx == -1 { return true }

	// Sauvegarde de l'état (Go copie les tableaux par valeur)
	backupG := *g
	backupRow := s.rowMask
	backupCol := s.colMask
	backupBox := s.boxMask

	for digit := uint16(0); digit < 9; digit++ {
		if (bestMask & (1 << digit)) != 0 {
			g[bestIdx] = byte('1' + digit)
			s.place(bestIdx, g[bestIdx])

			if s.solve(g) { return true }

			// Restauration
			*g = backupG
			s.rowMask = backupRow
			s.colMask = backupCol
			s.boxMask = backupBox
		}
	}
	return false
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	solver := &Solver{}
	for scanner.Scan() {
		line := scanner.Text()
		if len(line) >= 81 {
			var grid Sudoku
			copy(grid[:], line[:81])
			solver.initMasks(&grid)
			if solver.solve(&grid) {
				fmt.Println(string(grid[:]))
			} else {
				fmt.Println("No solution")
			}
		}
	}
}