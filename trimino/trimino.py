

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
    else:
        if(col%2 == 0): # col par = coluna inicial do bloco minimo
           for (x,y) in tiles[4]:
               matriz[line+x][col +y] = 4
        else:
            for (x,y) in tiles[1]:
               matriz[line+x][col +y] = 1 


solveSmallBlock(line,col,matriz)

print(matriz)

def solveMatriz(line, col, size,matriz):
    centerSquareSize = size/2
    startDifference = (size - centerSquareSize)/2

    if (size == 2):
        

    #if centerSquare is not solved, solve center:
    if(not centerSolved(line + startDifference,col + startDifference, centerSquareSize,matriz)):
        solveMatriz(line + startDifference,col + startDifference, centerSquareSize,matriz)
    #else if centerSquare is solved, solve each quadrant:
        quadrantSize = size/2
        #solve NW quadrant
        solveMatriz(line,col,quadrantSize,matriz)
        #solve SW
        solveMatriz(line+quadrantSize,col,quadrantSize,matriz)
        #solve NE
        solveMatriz(line,col+quadrantSize,quadrantSize,matriz)
        #solve SE
        solveMatriz(line+quadrantSize,col+quadrantSize,quadrantSize,matriz)



def centerSolved(lineStart,colStart,size,matriz):
    if(matriz[lineStart][colStart] == 0):
        return False
    elif (matriz[lineStart +size -1][colStart] == 0):
        return False
    elif (matriz[lineStart][colStart + size -1] == 0):
        return False
    elif(matriz[lineStart + size -1][colStart +size -1] == 0):
        return False
    else:
        return True
