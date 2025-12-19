//INFO: algo with arrays (optimized by copilot)
package main

import (
	"bufio"
	"fmt"
	"os"
)

// count number of set bits - using manual bit manipulation
func popcount(x uint16) int {
	x -= (x >> 1) & 0x5555
	x = (x & 0x3333) + ((x >> 2) & 0x3333)
	x = (x + (x >> 4)) & 0x0F0F
	return int((x * 0x0101) >> 8)
}

// fast path for getting free numbers using bitmask
func freeMask(g []byte, pos int) uint16 {
	var used uint16
	
	x := pos % 9
	y := pos / 9
	
	// Check row - unrolled
	row_start := y * 9
	if c := g[row_start]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[row_start+1]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[row_start+2]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[row_start+3]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[row_start+4]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[row_start+5]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[row_start+6]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[row_start+7]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[row_start+8]; c != '.' {
		used |= 1 << (c - '0')
	}
	
	// Check column - unrolled
	if c := g[x]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[9+x]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[18+x]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[27+x]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[36+x]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[45+x]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[54+x]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[63+x]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[72+x]; c != '.' {
		used |= 1 << (c - '0')
	}
	
	// Check 3x3 box
	box_x := (x / 3) * 3
	box_y := (y / 3) * 3
	b0 := (box_y * 9) + box_x
	if c := g[b0]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[b0+1]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[b0+2]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[b0+9]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[b0+10]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[b0+11]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[b0+18]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[b0+19]; c != '.' {
		used |= 1 << (c - '0')
	}
	if c := g[b0+20]; c != '.' {
		used |= 1 << (c - '0')
	}
	
	return ^used & 0x3FE // invert and mask bits 1-9
}

// resolv solves the Sudoku grid using backtracking
func resolv(g []byte) bool {
	// Find cell with minimum possibilities
	ibest := -1
	var cbest uint16
	minCount := 10

	for i := 0; i < 81; i++ {
		if g[i] == '.' {
			mask := freeMask(g, i)
			if mask == 0 {
				return false
			}
			cnt := popcount(mask)
			if cnt < minCount {
				minCount = cnt
				ibest = i
				cbest = mask
				if cnt == 1 {
					break
				}
			}
		}
	}

	if ibest >= 0 {
		// Try each possibility
		if (cbest & (1 << 1)) != 0 {
			g[ibest] = '1'
			if resolv(g) {
				return true
			}
			g[ibest] = '.'
		}
		if (cbest & (1 << 2)) != 0 {
			g[ibest] = '2'
			if resolv(g) {
				return true
			}
			g[ibest] = '.'
		}
		if (cbest & (1 << 3)) != 0 {
			g[ibest] = '3'
			if resolv(g) {
				return true
			}
			g[ibest] = '.'
		}
		if (cbest & (1 << 4)) != 0 {
			g[ibest] = '4'
			if resolv(g) {
				return true
			}
			g[ibest] = '.'
		}
		if (cbest & (1 << 5)) != 0 {
			g[ibest] = '5'
			if resolv(g) {
				return true
			}
			g[ibest] = '.'
		}
		if (cbest & (1 << 6)) != 0 {
			g[ibest] = '6'
			if resolv(g) {
				return true
			}
			g[ibest] = '.'
		}
		if (cbest & (1 << 7)) != 0 {
			g[ibest] = '7'
			if resolv(g) {
				return true
			}
			g[ibest] = '.'
		}
		if (cbest & (1 << 8)) != 0 {
			g[ibest] = '8'
			if resolv(g) {
				return true
			}
			g[ibest] = '.'
		}
		if (cbest & (1 << 9)) != 0 {
			g[ibest] = '9'
			if resolv(g) {
				return true
			}
			g[ibest] = '.'
		}
		return false
	}
	return true
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		input := scanner.Bytes()
		if len(input) != 81 {
			continue
		}
		
		g := make([]byte, 81)
		copy(g, input)
		
		if resolv(g) {
			fmt.Println(string(g))
		} else {
			fmt.Println("")
		}
	}
}
