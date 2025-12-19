//INFO: algo OPTIMIZED (by copilot)
#include <stdio.h>
#include <string.h>
#include <stdint.h>

#define POPCOUNT(x) __builtin_popcount((unsigned int)(x))
#define CTZ(x) __builtin_ctz((unsigned int)(x))

static uint16_t row_mask[9];
static uint16_t col_mask[9];
static uint16_t box_mask[9];

static inline void init_masks(const char *g) {
    for (int i = 0; i < 9; i++) {
        row_mask[i] = col_mask[i] = box_mask[i] = 0;
    }
    for (int i = 0; i < 81; i++) {
        if (g[i] != '.') {
            uint16_t bit = 1 << (g[i] - '1');
            row_mask[i / 9] |= bit;
            col_mask[i % 9] |= bit;
            box_mask[(i / 27) * 3 + (i % 9) / 3] |= bit;
        }
    }
}

static inline uint16_t get_candidates(int idx) {
    int row = idx / 9, col = idx % 9, box = (row / 3) * 3 + (col / 3);
    return 0x1FF & ~(row_mask[row] | col_mask[col] | box_mask[box]);
}

static inline void place(int idx, char val) {
    uint16_t bit = 1 << (val - '1');
    int row = idx / 9, col = idx % 9, box = (row / 3) * 3 + (col / 3);
    row_mask[row] |= bit;
    col_mask[col] |= bit;
    box_mask[box] |= bit;
}

// Propagation de contraintes: naked singles et hidden singles optimisée
static int propagate(char *g) {
    // Phase 1: Remplir toutes les cellules avec une seule possibilité
    int changed = 1;
    int iterations = 0;
    while (changed && iterations < 15) {
        changed = 0;
        iterations++;
        
        for (int i = 0; i < 81; i++) {
            if (g[i] == '.') {
                uint16_t cand = get_candidates(i);
                if (cand == 0) return 0;
                int pop = POPCOUNT(cand);
                if (pop == 1) {
                    g[i] = '1' + CTZ(cand);
                    place(i, g[i]);
                    changed = 1;
                }
            }
        }
    }
    
    // Phase 2: Hidden singles en lignes
    for (int row = 0; row < 9; row++) {
        for (int digit = 0; digit < 9; digit++) {
            if (row_mask[row] & (1 << digit)) continue;
            int count = 0, last_col = -1;
            for (int col = 0; col < 9; col++) {
                int idx = row * 9 + col;
                if (g[idx] == '.' && (get_candidates(idx) & (1 << digit))) {
                    count++;
                    last_col = col;
                    if (count > 1) break;
                }
            }
            if (count == 0) return 0;
            if (count == 1 && g[row * 9 + last_col] == '.') {
                g[row * 9 + last_col] = '1' + digit;
                place(row * 9 + last_col, g[row * 9 + last_col]);
            }
        }
    }
    
    // Phase 3: Hidden singles en colonnes
    for (int col = 0; col < 9; col++) {
        for (int digit = 0; digit < 9; digit++) {
            if (col_mask[col] & (1 << digit)) continue;
            int count = 0, last_row = -1;
            for (int row = 0; row < 9; row++) {
                int idx = row * 9 + col;
                if (g[idx] == '.' && (get_candidates(idx) & (1 << digit))) {
                    count++;
                    last_row = row;
                    if (count > 1) break;
                }
            }
            if (count == 0) return 0;
            if (count == 1 && g[last_row * 9 + col] == '.') {
                g[last_row * 9 + col] = '1' + digit;
                place(last_row * 9 + col, g[last_row * 9 + col]);
            }
        }
    }
    
    return 1;
}

// Résolution avec MRV + backtracking optimisé
int resolv(char *g) {
    if (!propagate(g)) return 0;
    
    int best_idx = -1, min_count = 10;
    uint16_t best_mask = 0;
    
    // Trouver la cellule vide avec le moins de candidats
    for (int i = 0; i < 81; i++) {
        if (g[i] == '.') {
            uint16_t cand = get_candidates(i);
            if (cand == 0) return 0;
            int cnt = POPCOUNT(cand);
            if (cnt < min_count) {
                min_count = cnt;
                best_idx = i;
                best_mask = cand;
                if (cnt == 1) break;
            }
        }
    }
    
    if (best_idx == -1) return 1;  // Puzzle résolu !
    
    // Sauvegarder l'état
    char backup[81];
    uint16_t backup_row[9], backup_col[9], backup_box[9];
    memcpy(backup, g, 81);
    memcpy(backup_row, row_mask, 18);
    memcpy(backup_col, col_mask, 18);
    memcpy(backup_box, box_mask, 18);
    
    // Essayer chaque candidat
    for (int digit = 0; digit < 9; digit++) {
        if (!(best_mask & (1 << digit))) continue;
        
        g[best_idx] = '1' + digit;
        place(best_idx, g[best_idx]);
        
        if (resolv(g)) return 1;
        
        memcpy(g, backup, 81);
        memcpy(row_mask, backup_row, 18);
        memcpy(col_mask, backup_col, 18);
        memcpy(box_mask, backup_box, 18);
    }
    
    return 0;
}

int main() {
    char line[128];
    while (fgets(line, sizeof(line), stdin)) {
        line[strcspn(line, "\r\n")] = 0;
        if (strlen(line) >= 81) {
            init_masks(line);
            if (resolv(line)) {
                printf("%s\n", line);
            } else {
                printf("No solution\n");
            }
        }
    }
    return 0;
}