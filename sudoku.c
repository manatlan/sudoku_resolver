//INFO: the simple algo, with strings (AI translation from java one) (100grids)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

char *sqr(const char *g, int x, int y) {
    x = (x / 3) * 3;
    y = (y / 3) * 3;
    char *result = malloc(10);
    strncpy(result, g + y * 9 + x, 3);
    strncpy(result + 3, g + y * 9 + x + 9, 3);
    strncpy(result + 6, g + y * 9 + x + 18, 3);
    result[9] = '\0';
    return result;
}

char *col(const char *g, int x) {
    char *result = malloc(10);
    for (int y = 0; y < 9; y++) {
        result[y] = g[x + y * 9];
    }
    result[9] = '\0';
    return result;
}

char *row(const char *g, int y) {
    char *result = malloc(10);
    strncpy(result, g + y * 9, 9);
    result[9] = '\0';
    return result;
}

void freeset(const char *g, bool *availableDigits) {
    for (int i = 0; i < 9; ++i) {
        availableDigits[i] = true;
    }

    while (*g != '\0') {
        if (*g >= '1' && *g <= '9') {
            availableDigits[*g - '1'] = false;
        }
        ++g;
    }
}

void free_digits(const char *g, int x, int y, bool *availableDigits) {
    char *currentRow = row(g, y);
    char *currentCol = col(g, x);
    char *currentSqr = sqr(g, x, y);
    char combinedSet[28];
    strcpy(combinedSet, currentRow);
    strcat(combinedSet, currentCol);
    strcat(combinedSet, currentSqr);

    freeset(combinedSet, availableDigits);

    free(currentRow);
    free(currentCol);
    free(currentSqr);
}

char *resolve(char *g, int index) {
    if (index >= 81) {
        return g;
    }

    if (g[index] != '.') {
        return resolve(g, index + 1);
    }

    bool availableDigits[9];
    free_digits(g, index % 9, index / 9, availableDigits);
    for (int i = 0; i < 9; ++i) {
        if (availableDigits[i]) {
            g[index] = i + '1';
            char *solution = resolve(g, index + 1);
            if (solution != NULL) {
                return solution;
            }
            g[index] = '.';
        }
    }
    return NULL;
}

int main() {
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("grids.txt", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    int nb=0;
    clock_t startTime = clock();
    while ((read = getline(&line, &len, fp)) != -1) {
        if (strchr(line, '\n'))
             line[strcspn(line, "\n")] = '\0';
        char *solution = resolve(line, 0);
        if (solution == NULL) {
            printf("not resolved ?!\n");
        } else {
            printf("%s\n", solution);
        }
        nb++;
        if(nb>99) break;
    }
    clock_t endTime = clock();

    float t=((float)endTime - (float)startTime)/1000000;
    printf("Took: %.6fs\n", t );

    fclose(fp);
    if (line)
        free(line);
    exit(EXIT_SUCCESS);
}
