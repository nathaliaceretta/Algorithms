

#Create an algotithm using backtracking that recieves a list of people and calculate how many ways we can arrange them lineraly.


people = ["b1","g1","b2"]

def arrange(elements):
    sum = 0
    if len(elements) == 1:
        return 1
    else:
        for i in range(len(elements)):
            element = elements.pop(i)
            sum += arrange(elements)
            elements.append(element)
    return sum


print(arrange(people))

#Now create an algorithm using backtracking to arrange a list of people but girls cant be seated in the second position.

def arrange2(elements):
    sum = 0
    if len(elements) == 1:
        return 1
    else:
        for i in range(len(elements)):
            if isPossible(elements,elements[i]):
                element = elements.pop(i)
                sum += arrange2(elements)
                elements.append(element)
    return sum

    

def isPossible(elements, element):
    if element =="g1" and len(elements) == 2:
            return False
    return True

print(arrange2(people))


#Now change the first algorithm to display all possible solutions on the console

def arrange3(elements):
    solutions = set()  # Conjunto para armazenar as soluções
    if len(elements) == 1:
        solutions.add(elements[0])  # Adiciona o único elemento quando a lista tem apenas um item
    else:
        for i in range(len(elements)):
            element = elements.pop(i)  # Remove o elemento atualujm 
            # Chamada recursiva
            sub_solutions = arrange3(elements)  # Chama a função recursivamente
            for solution in sub_solutions:
                solutions.add(element + solution)  # Concatena o elemento atual com as soluções retornadas
            elements.insert(i, element)  # Restaura o elemento na posição correta
    return solutions

print(arrange3(people))

