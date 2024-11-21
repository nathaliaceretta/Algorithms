

#dictionary of tiles, where the key represent the type of tile and the list contains the  positions of the building blocks of each tile relative to the missing block considered. 

tiles = {
    1 : [(-1,-1), (-1,0),(0,-1)],
    2 :[(0,-1),(+1,-1), (+1,0)],
    3: [(0,+1),(+1,-1),(+1,0)],
    4: [(-1,0),(-1,+1),(0,+1)]
}

n = int(input())

size = 2**n

matriz = [[0 for _ in range(size)] for _ in range(size)]

line = 2**(n-1) 
col = 2**(n-2) 

print(line)
print(col)


matriz[line][col] = "x"
print(matriz)

print(len(matriz))


def solveSmallBlock(line, col,matriz):
    if(line%2 == 0): #linha par = começo de um bloco minimo
        if(col%2 == 0): # col par = coluna inicial do bloco minimo
           for (x,y) in tiles[3]:
               matriz[line+x][col +y] = 3
        else:
            for (x,y) in tiles[2]:
               matriz[line+x][col +y] = 2


solveSmallBlock(line,col,matriz)

print(matriz)