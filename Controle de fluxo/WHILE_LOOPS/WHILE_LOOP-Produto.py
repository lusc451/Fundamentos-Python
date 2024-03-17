# == While loops ====
#EXCELENTE PARA LOOPS DEPENDENTES DE UMA CONDIÇÃO

#CRIAR UMA PROMOÇÃO PARA UM PRODUTO NO VALOR DE R$100.

valor = 100
dia = 0

while valor > 20:
    dia += 1
    print(f' No {dia} o produto vai ser vendido por R${valor}')
    valor -= 5