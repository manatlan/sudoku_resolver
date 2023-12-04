//INFO: algo with strings
package main

import (
	"fmt"
	"strings"
)

// sqr returns the square of the Sudoku grid at the specified coordinates.
func sqr(g string, x, y int) string {
	x = (x / 3) * 3
	y = (y / 3) * 3
	return g[y*9+x:y*9+x+3] + g[y*9+x+9:y*9+x+12] + g[y*9+x+18:y*9+x+21]
}

// col returns the column of the Sudoku grid at the specified column index.
func col(g string, x int) string {
	var result strings.Builder
	for y := 0; y < 9; y++ {
		ligne := y * 9
		result.WriteByte(g[x+ligne])
	}
	return result.String()
}

// row returns the row of the Sudoku grid at the specified row index.
func row(g string, y int) string {
	ligne := y * 9
	return g[ligne : ligne+9]
}

// free returns the set of free numbers at the specified coordinates in the Sudoku grid.
func free(g string, x, y int) string {
	all := "123456789"
	t27 := row(g, y) + col(g, x) + sqr(g, x, y)
	var freeset strings.Builder

	for i := 0; i < 9; i++ {
		c := all[i]
		if strings.IndexByte(t27,c) < 0 {
			freeset.WriteByte(c)
		}
	}
	return freeset.String()
}

// resolv solves the Sudoku grid using backtracking.
func resolv(g string) string {
	ibest := -1
	cbest := "123456789"

	for i := 0; i < 81; i++ {
		if g[i] == '.' {
			c := free(g, i%9, i/9)
			if len(c) == 0 {
				return ""
			}
			if len(c) < len(cbest) {
				ibest = i
				cbest = c
			}
			if len(c) == 1 {
				break
			}
		}
	}

	if ibest >= 0 {
		for j := 0; j < len(cbest); j++ {
			elem := cbest[j]
			ng := resolv(g[:ibest] + string(elem) + g[ibest+1:])
			if ng != "" {
				return ng
			}
		}
		return ""
	} else {
		return g
	}
}

func main() {
	var input string
	for {
		_, err := fmt.Scanln(&input)
		if err != nil {
			break
		}
		fmt.Println(resolv(input))
	}
}
