#!./make.py
#INFO: algo with specialized types/logics (optimized by copilot)

import sys

def solve(grid_str):
    # Initialisation des structures de données
    board = [int(c) if c != '.' else 0 for c in grid_str]
    rows = [0] * 9
    cols = [0] * 9
    blocks = [0] * 9
    
    # Pré-calculer block_idx pour chaque position
    block_idx_map = [(i // 27) * 3 + (i % 9) // 3 for i in range(81)]
    
    # Fonction pour compter les bits (compatible Python 3.9+ et Codon)
    def bit_count(mask):
        count = 0
        while mask:
            count += 1
            mask &= mask - 1
        return count
    
    # Table de lookup pour compter les options rapidement
    option_count = [9 - bit_count(mask >> 1) for mask in range(1024)]
    
    # Remplissage initial et détection des cases vides
    empty_cells = []
    for i in range(81):
        r, c = divmod(i, 9)
        val = board[i]
        if val > 0:
            mask = 1 << val
            rows[r] |= mask
            cols[c] |= mask
            blocks[block_idx_map[i]] |= mask
        else:
            empty_cells.append(i)

    def backtrack():
        # Appliquer constraint propagation avec naked singles
        changed = True
        while changed:
            changed = False
            i = 0
            while i < len(empty_cells):
                cell_idx = empty_cells[i]
                r, c = divmod(cell_idx, 9)
                forbidden = rows[r] | cols[c] | blocks[block_idx_map[cell_idx]]
                opts = option_count[forbidden]
                
                if opts == 0:
                    return False  # Cul-de-sac
                elif opts == 1:  # Naked single - on le remplit
                    # Trouver la valeur unique
                    for val in range(1, 10):
                        if not (forbidden & (1 << val)):
                            mask = 1 << val
                            board[cell_idx] = val
                            rows[r] |= mask
                            cols[c] |= mask
                            blocks[block_idx_map[cell_idx]] |= mask
                            break
                    empty_cells[i] = empty_cells[-1]
                    empty_cells.pop()
                    changed = True
                else:
                    i += 1
        
        if not empty_cells:
            return True

        # Heuristique MRV : on cherche la case avec le moins de possibilités
        best_idx = 0
        min_options = 10

        for i in range(len(empty_cells)):
            cell_idx = empty_cells[i]
            r, c = divmod(cell_idx, 9)
            forbidden = rows[r] | cols[c] | blocks[block_idx_map[cell_idx]]
            opts = option_count[forbidden]
            
            if opts == 1: # Priorité absolue si une seule option
                best_idx = i
                break
            if opts < min_options:
                min_options = opts
                best_idx = i
        
        cell_idx = empty_cells[best_idx]
        empty_cells[best_idx] = empty_cells[-1]
        empty_cells.pop()
        
        r, c = divmod(cell_idx, 9)
        b = block_idx_map[cell_idx]
        forbidden = rows[r] | cols[c] | blocks[b]
        
        # Sauvegarder les états
        saved_board = board.copy()
        saved_rows = rows.copy()
        saved_cols = cols.copy()
        saved_blocks = blocks.copy()
        saved_empty = empty_cells.copy()

        for val in range(1, 10):
            mask = 1 << val
            if not (forbidden & mask):
                # Placement
                board[cell_idx] = val
                rows[r] |= mask
                cols[c] |= mask
                blocks[b] |= mask
                
                if backtrack():
                    return True
                
                # Restaurer depuis la sauvegarde
                for j in range(81):
                    board[j] = saved_board[j]
                for j in range(9):
                    rows[j] = saved_rows[j]
                    cols[j] = saved_cols[j]
                    blocks[j] = saved_blocks[j]
                empty_cells[:] = saved_empty
        
        return False

    if backtrack():
        return "".join(map(str, board))
    return "Pas de solution"


for line in sys.stdin:
    line = line.strip()
    if line:
        print(solve(line))

