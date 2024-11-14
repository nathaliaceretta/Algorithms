import sys
import time


mapSize = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])


tabuleiro = [["_" for _ in range(mapSize)] for _ in range(mapSize)]
solutions = set()


def salao(b, c, map, solutions,startB,startC):
    if b == 0 and c == 0:
        if checaTabuleiro(map):
            solutions.add(tuple(tuple(row) for row in map))
        return
    
    if b < 0 or c < 0:
        return

    #adding B
    size = len(map)
    if(b>0):
        for z in range(startB, size*size):
            i, j = divmod(z, size)
            if map[i][j] == "_" and notContiguous(i, j, map):
                map[i][j] = "b"
                salao(b-1, c, map, solutions,z+1,startC)
                map[i][j] = "_"

    if c>0:
        for z in range(startC, size*size):
            i, j = divmod(z, size)
            if map[i][j]=="_" and isValid(i, j, map, "c", "b"):
                map[i][j] = "c"
                salao(b, c-1, map, solutions,startB,z+1)
                map[i][j] = "_"


    return solutions


def notContiguous(l, c, map):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in directions:
        if 0 <= l + dr < len(map) and 0 <= c + dc < len(map):
            if map[l + dr][c + dc] == "b":
                return False
    return True


def isValid(l, c, map, pistoleiro, enemy):
    enemySeen = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in directions:
        for step in range(1, mapSize):
            r, d = l + dr * step, c + dc * step
            if not (0 <= r < mapSize and 0 <= d < mapSize):
                break
            if map[r][d] == pistoleiro:
                return False
            if map[r][d] == enemy:
                enemySeen += 1
                break


    return enemySeen >= 2


def checaTabuleiro(map):
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == "b":
                if not isValid(i, j, map, "b", "c"):
                    return False
    return True


inicio = time.time() 
soluçoes = salao(b, c, tabuleiro, solutions,0,0)
print(len(soluçoes))
fim = time.time() 

tempo_execucao = fim - inicio
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
