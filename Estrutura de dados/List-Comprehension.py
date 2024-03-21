#List Comprehension
    #Mais simples de se escrever
    #Utilizado quando você precisa criar uma nova lista a partir de uma existente
    # [expressao for iten in itens]
    
frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
#Selecionar somente as frutas com a letra B
# frutas2 = []

# for itens in frutas1:
#     if 'n' in itens:
#         frutas2.append(itens)

frutas2 = [iten for iten in frutas1 if 'k' in iten]

print(frutas2)