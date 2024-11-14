#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

int mapSize;
int b;
int c;

char **createBoard(int size) {
    char **board = (char **)malloc(size * sizeof(char *));
    for (int i = 0; i < size; i++) {
        board[i] = (char *)malloc(size * sizeof(char));
        for (int j = 0; j < size; j++) {
            board[i][j] = '_';
        }
    }
    return board;
}

void freeBoard(char **board, int size) {
    for (int i = 0; i < size; i++) {
        free(board[i]);
    }
    free(board);
}

bool notContiguous(int l, int c, char **map) {
    int directions[8][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1},
                             {-1, -1}, {-1, 1}, {1, -1}, {1, 1} };
    
    for (int i = 0; i < 8; i++) {
        int dr = directions[i][0];
        int dc = directions[i][1];
        if (l + dr >= 0 && l + dr < mapSize && c + dc >= 0 && c + dc < mapSize) {
            if (map[l + dr][c + dc] == 'b') {
                return false;
            }
        }
    }
    return true;
}

bool isValid(int l, int c, char **map, char pistoleiro, char enemy) {
    int enemySeen = 0;
    int directions[8][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1},
                             {-1, -1}, {-1, 1}, {1, -1}, {1, 1} };
    
    for (int i = 0; i < 8; i++) {
        int dr = directions[i][0];
        int dc = directions[i][1];
        for (int step = 1; step < mapSize; step++) {
            int r = l + dr * step;
            int d = c + dc * step;
            if (r < 0 || r >= mapSize || d < 0 || d >= mapSize) {
                break;
            }
            if (map[r][d] == pistoleiro) {
                return false;
            }
            if (map[r][d] == enemy) {
                enemySeen++;
                break;
            }
        }
    }
    return enemySeen >= 2;
}

bool checaTabuleiro(char **map) {
    for (int i = 0; i < mapSize; i++) {
        for (int j = 0; j < mapSize; j++) {
            if (map[i][j] == 'b') {
                if (!isValid(i, j, map, 'b', 'c')) {
                    return false;
                }
            }
        }
    }
    return true;
}

int salao(int b, int c, char **map, int startB, int startC) {
    int sum = 0;
    if (b == 0 && c == 0) {
        if (checaTabuleiro(map)) {
            return 1;
        }
        return 0;
    }

    if (b < 0 || c < 0) {
        return 0;
    }

    int size = mapSize;
    if (b > 0) {
        for (int z = startB; z < size * size; z++) {
            int i = z / size;
            int j = z % size;
            if (map[i][j] == '_' && notContiguous(i, j, map)) {
                map[i][j] = 'b';
                sum += salao(b - 1, c, map, z + 1, startC);
                map[i][j] = '_';
            }
        }
    } else if (c > 0) {
        for (int z = startC; z < size * size; z++) {
            int i = z / size;
            int j = z % size;
            if (map[i][j] == '_' && isValid(i, j, map, 'c', 'b')) {
                map[i][j] = 'c';
                sum += salao(b, c - 1, map, startB, z + 1);
                map[i][j] = '_';
            }
        }
    }

    return sum;
}

int main(int argc, char *argv[]) {
    if (argc < 4) {
        printf("Usage: %s mapSize b c\n", argv[0]);
        return 1;
    }

    mapSize = atoi(argv[1]);
    b = atoi(argv[2]);
    c = atoi(argv[3]);

    char **tabuleiro = createBoard(mapSize);

    clock_t inicio = clock();
    int solucoes = salao(b, c, tabuleiro, 0, 0);
    clock_t fim = clock();

    double tempo_execucao = (double)(fim - inicio) / CLOCKS_PER_SEC;
    printf("Soluções: %d\n", solucoes);
    printf("Tempo de execução: %.6f segundos\n", tempo_execucao);

    freeBoard(tabuleiro, mapSize);
    return 0;
}
