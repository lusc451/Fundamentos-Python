from sys import getsizeof

#Generator Expressions
    #Uma forma mais rápida para listas, dicionários, etc.
    #Menos memória alocada
    #Valores em bytes
    
numeros = [x * 10 for x in range(10)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))

print('=========')

numeros = (x * 10 for x in range(10))
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))