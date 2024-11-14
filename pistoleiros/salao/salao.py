import sys
import time

mapSize = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])


tabuleiro = [["_" for _ in range(mapSize)] for _ in range(mapSize)]
tabuleiros = set()


def salao(b, c, map, solutions,first):
    if b == 0 and c == 0:
        if checaTabuleiro(map):
            solutions.add(tuple(tuple(row) for row in map))
            for i in range(4):
                map = rotaTabuleiro(map)
                solutions.add(tuple(tuple(row) for row in map))
            """ for row in map:
                print(" ".join(row)) """
        return

    if b < 0 or c < 0:
        return



   
    #primeiro b
    if first:
        for i in range((len(map)+1)//2):
            for j in range((len(map)+1)//2):
                if b>0 and notContiguous(i, j, map):
                    map[i][j] = "b"
                    b -= 1
                    salao(b, c, map, solutions,False)
                    b += 1
                    map[i][j] = "_"
                   
       

    # Primeira adição de b
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] =="_" and notContiguous(i, j, map) and b > 0:
                map[i][j] = "b"
                b -= 1
                salao(b, c, map, solutions,False)
                b += 1
                map[i][j] = "_"


    # Adição de c
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j]=="_" and isValid(i, j, map, "c", "b") and c > 0:
                c -= 1
                map[i][j] = "c"
                salao(b, c, map, solutions,False)
                c += 1
                map[i][j] = "_"


    return solutions


def notContiguous(l, c, map):
    # check all directions
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




def rotaTabuleiro(tabuleiro):
    size = len(tabuleiro)
    rotado = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            rotado[j][size-1-i] = tabuleiro[i][j]
    return rotado



inicio = time.time() 
print(len(salao(b, c, tabuleiro, tabuleiros,True)))
fim = time.time() 
tempo_execucao = fim - inicio
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
