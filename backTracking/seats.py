
# How many ways can you arrange n people in n seats using backtracking

#ex 2 boys: b1 b2 e 1 girl g1


def seat(n):
    if n == 1: 
        return 1
    else:
        return n*seat(n-1)
    
print(seat(4))


#Now, I have 2 boys and 1 girl. Girl cant be in the middle. This is a restriction (bound function)

elements = ["b1","b2","g1"]
picked = []
sum = 0

def arrange(elements,picked):
    if len(elements) == 1:
        return 1
    else:
        soma = 0
        for i in range(len(elements)):
            if elements[i] not in picked and sit(picked,elements[i]):
                picked.append(elements[i])
                elements.remove(elements[i])
                soma += arrange(elements,picked)
                elements.append(picked.pop())
    return soma
    

def sit(picked, element):
    if len(picked) == 1 and element == "g1":
        return False
    else:
        return True 


print(arrange(elements,picked))
