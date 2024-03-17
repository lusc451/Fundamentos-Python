#Functions (Funções)
    #DRY - Don't Repeat Yourself.
    #Vários argumentos (xargs)
#CRIAR UMA FUNÇÃO QUE SOMA VÁRIOS NÚMEROS

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x = soma(2, 3, 4, 7, 4)
print(x)