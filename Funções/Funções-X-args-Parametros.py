#Functions (Funções)
    #DRY - Don't Repeat Yourself.
    #Vários argumentos (xargs) identificando parametros
    
#CRIAR UMA FUNÇÃO QUE ARMAZENA NUMEROS E STRINGS (DADOS)

def agencia(**carro): #1 ASTERISCO = VARIOS ARGUMENTOS; 2 ASTERISCOS = VARIOS ARGUMENTOS E PARAMETROS
    return carro

print(agencia(modelo='Gol', cor='Branco', motor=1.0, placa=1234))
print(agencia(modelo='Corsa', cor='Cinza', motor=1.6))
print(agencia(modelo='Celta', cor='Preto'))