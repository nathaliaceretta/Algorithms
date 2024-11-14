
#adding queens just not in the same row and not in the same column

queens = 4

map =[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

colOcuppied = set()
def addQueen(queensLeft,colOcuppied):
    sum = 0

    if(queensLeft == 0):
        return 1
    for i in range(3):
        if(i not in colOcuppied):
            queensLeft -=1
            colOcuppied.add(i)
            sum += addQueen(queensLeft,colOcuppied)
            queensLeft +=1
            colOcuppied.remove(i)
       

    return sum

""" print(addQueen(3,colOcuppied)) """

#

def addQueen2(queensLeft,map,currentLine,colOcuppied):
    sum = 0

    if(queensLeft == 0):
        return 1
    for i in range(len(map)):
        if(i not in colOcuppied and notSeen(map,currentLine,i)):
            queensLeft -=1
            colOcuppied.add(i)
            map[currentLine][i] = 1
            sum += addQueen2(queensLeft,map,currentLine +1,colOcuppied)
            map[currentLine][i] = 0
            queensLeft +=1
            colOcuppied.remove(i)
    return sum

def notSeen(map,l,c):
    if(l == 0):
        return True
   
    #diagonais Norte
    colPos = c
    colMin = c
    for i in range(l-1,-1,-1):
        colPos += 1
        if(colPos < len(map) and map[i][colPos] == 1):
            return False
        colMin -=1
        if(colMin>= 0 and map[i][colMin] == 1):
                return False

    return True
        

print(addQueen2(4,map,0,colOcuppied))

