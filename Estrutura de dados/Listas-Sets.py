
#Set (Listas)
    #Similar a listas
    #Evita itens duplicados
    #Não utiliza index
    
list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) #Union - Unifica as listas, removendo itens repetidos
print(num1 - num2) #Difference - Mostra somente os itens que não estão repetidos na segunda lista
print(num1 ^ num2) #Symmetric Difference - Remove todos os itens duplicados nas duas listas
print(num1 & num2) #And - Mostra somente os itens duplicados em ambas as listas

print(len(num1))
print(len(num2))