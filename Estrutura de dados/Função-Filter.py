#Filter Function
    #Muito Utilizado com listas
    #Aplicar uma função Iterable, filtrando os items. (list, tuple, etc)

valores = [10, 12, 34, 44, 57]

# def remover20(x):
#     return x > 20

# print(list(filter(remover20, valores)))

print(list(filter(lambda x: x > 20, valores)))