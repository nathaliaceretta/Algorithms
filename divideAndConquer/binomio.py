




def binomio(l,c):
    v = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    for i in range(1,l+1):
        v[i][1]= 1
        v[i][i] =1
        for j in range(2,c+1):
            v[i][j]= v[i-1][j]+ v[i-1][j-1]
    return v[l][c]


print(binomio(6,3))
     
