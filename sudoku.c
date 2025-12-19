//INFO: algo with strings (made by gemini3 from py version)
#include <stdio.h>
#include <string.h>

// Calcule les chiffres disponibles pour une case (x, y)
// Retourne un masque de bits où le bit n est à 1 si le chiffre n est libre
unsigned short get_free(const char *g, int x, int y) {
    unsigned short used = 0;
    int i, j;
    
    // Check ligne et colonne
    for (i = 0; i < 9; i++) {
        if (g[y * 9 + i] != '.') used |= (1 << (g[y * 9 + i] - '1'));
        if (g[i * 9 + x] != '.') used |= (1 << (g[i * 9 + x] - '1'));
    }
    
    // Check carré 3x3
    int start_x = (x / 3) * 3;
    int start_y = (y / 3) * 3;
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            char c = g[(start_y + i) * 9 + (start_x + j)];
            if (c != '.') used |= (1 << (c - '1'));
        }
    }
    
    return ~used & 0x1FF; // On retourne l'inverse des bits utilisés (limité aux 9 premiers bits)
}

// Compte le nombre de bits à 1 (nombre de possibilités)
int count_bits(unsigned short v) {
    int c;
    for (c = 0; v; c++) v &= v - 1;
    return c;
}

int resolv(char *g) {
    int ibest = -1;
    int min_avails = 10;
    unsigned short best_mask = 0;

    // Heuristic: Recherche de la case avec le moins de possibilités (MRV)
    for (int i = 0; i < 81; i++) {
        if (g[i] == '.') {
            unsigned short mask = get_free(g, i % 9, i / 9);
            int count = count_bits(mask);
            
            if (count == 0) return 0; // Cul-de-sac

            if (count < min_avails) {
                min_avails = count;
                ibest = i;
                best_mask = mask;
                if (count == 1) break; // Optimisation : si une seule possibilité, on fonce
            }
        }
    }

    if (ibest == -1) return 1; // Terminé !

    // Backtracking
    for (int c = 0; c < 9; c++) {
        if (best_mask & (1 << c)) {
            g[ibest] = (char)('1' + c);
            if (resolv(g)) return 1;
            g[ibest] = '.'; // Backtrack
        }
    }

    return 0;
}

int main() {
    char line[128];
    while (fgets(line, sizeof(line), stdin)) {
        // Nettoyage du saut de ligne
        line[strcspn(line, "\r\n")] = 0;
        if (strlen(line) >= 81) {
            if (resolv(line)) {
                printf("%s\n", line);
            } else {
                printf("No solution\n");
            }
        }
    }
    return 0;
}