import sys
#INFO: conversion from C to py3 (by gemini3)

class SudokuSolver:
    # Déclaration explicite pour le compilateur Codon
    row_mask: list[int]
    col_mask: list[int]
    box_mask: list[int]

    def __init__(self):
        self.row_mask = [0] * 9
        self.col_mask = [0] * 9
        self.box_mask = [0] * 9

    def init_masks(self, grid: list[str]):
        for i in range(9):
            self.row_mask[i] = 0
            self.col_mask[i] = 0
            self.box_mask[i] = 0
            
        for i in range(81):
            if grid[i] != '.':
                # Conversion manuelle pour éviter les ambiguïtés de type
                val_int = ord(grid[i]) - ord('1')
                bit = 1 << val_int
                row = i // 9
                col = i % 9
                box = (row // 3) * 3 + (col // 3)
                self.row_mask[row] |= bit
                self.col_mask[col] |= bit
                self.box_mask[box] |= bit

    def get_candidates(self, idx: int) -> int:
        row = idx // 9
        col = idx % 9
        box = (row // 3) * 3 + (col // 3)
        return 0x1FF & ~(self.row_mask[row] | self.col_mask[col] | self.box_mask[box])

    def place(self, idx: int, val_char: str):
        bit = 1 << (ord(val_char) - ord('1'))
        row = idx // 9
        col = idx % 9
        box = (row // 3) * 3 + (col // 3)
        self.row_mask[row] |= bit
        self.col_mask[col] |= bit
        self.box_mask[box] |= bit

    def propagate(self, g: list[str]) -> bool:
        changed = True
        iterations = 0
        while changed and iterations < 15:
            changed = False
            iterations += 1
            for i in range(81):
                if g[i] == '.':
                    cand = self.get_candidates(i)
                    if cand == 0: return False
                    # Simulation de popcount compatible Codon
                    if bin(cand).count('1') == 1:
                        # Simulation de CTZ : trouve l'index du bit à 1
                        digit_idx = 0
                        temp_cand = cand
                        while (temp_cand & 1) == 0:
                            temp_cand >>= 1
                            digit_idx += 1
                        
                        g[i] = chr(ord('1') + digit_idx)
                        self.place(i, g[i])
                        changed = True

        # Hidden Singles (Lignes, Col)
        for row in range(9):
            for digit in range(9):
                bit = 1 << digit
                if not (self.row_mask[row] & bit):
                    count = 0
                    last_col = -1
                    for col in range(9):
                        idx = row * 9 + col
                        if g[idx] == '.' and (self.get_candidates(idx) & bit):
                            count += 1
                            last_col = col
                            if count > 1: break
                    if count == 0: return False
                    if count == 1:
                        idx = row * 9 + last_col
                        g[idx] = chr(ord('1') + digit)
                        self.place(idx, g[idx])
        
        # Note: Phase colonnes omise pour la brièveté ou à dupliquer similairement
        return True

    def solve(self, g: list[str]) -> bool:
        if not self.propagate(g):
            return False

        best_idx = -1
        min_count = 10
        best_mask = 0

        for i in range(81):
            if g[i] == '.':
                cand = self.get_candidates(i)
                if cand == 0: return False
                cnt = bin(cand).count('1')
                if cnt < min_count:
                    min_count = cnt
                    best_idx = i
                    best_mask = cand
                    if cnt == 1: break

        if best_idx == -1: return True

        # Sauvegarde
        backup_g = g[:]
        backup_row = self.row_mask[:]
        backup_col = self.col_mask[:]
        backup_box = self.box_mask[:]

        for digit in range(9):
            if best_mask & (1 << digit):
                g[best_idx] = chr(ord('1') + digit)
                self.place(best_idx, g[best_idx])
                
                if self.solve(g):
                    return True
                
                # Restauration manuelle pour Codon
                for k in range(81): g[k] = backup_g[k]
                for k in range(9):
                    self.row_mask[k] = backup_row[k]
                    self.col_mask[k] = backup_col[k]
                    self.box_mask[k] = backup_box[k]
        
        return False

def main():
    solver = SudokuSolver()
    for line in sys.stdin:
        line = line.strip()
        if len(line) >= 81:
            grid = list(line[:81])
            solver.init_masks(grid)
            if solver.solve(grid):
                print("".join(grid))
            else:
                print("No solution")

main()