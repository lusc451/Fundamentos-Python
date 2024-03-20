#Map Function
    #Muito utilizado com listas
    #Aplicar uma função Iterable, por item. (list, tuple, dic, etc.)
    
lista1 = [2, 4, 6, 8, 10, 12]

# lista2 = map(lambda x: x * 2, lista1)

print(list(map(lambda x: x + 10, lista1)))




# def multi(x):
#     return x * 2

# lista2 = map(multi, lista1)