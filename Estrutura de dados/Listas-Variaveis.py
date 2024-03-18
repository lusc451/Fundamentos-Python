#Listas
    #Armazenar mais de uma informação em variáveis
    #Manter a sequência dos dados em uma variável

produtos = ['arroz', 'feijão', 'laranja', 'banana', 1, 2, 3, 4]

item1, item2, item3, *outros = produtos

# item1 = produtos[0]
# item2 = produtos[1]
# item3 = produtos[2]
# item4 = produtos[3]

print(item1)
print(item2)
print(item3)
# print(item4)
print(outros)