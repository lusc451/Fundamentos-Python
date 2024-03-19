#Tuples
    #Armazenar mais de uma informação em variáveis
    #Manter a sequência dos dados em uma variável
    #NÃO PODEM SER ALTERADAS (IMMUTABLE)

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho') #ENTRE PARENTESES

# print(type(cores_list))
# print(type(cores_tuple))

# duas = cores_tuple * 2
# print(duas)

cores_list.append('roxo')
print(cores_list)

# cores_tuple.append('roxo') ----- ERRO - LISTA IMUTÁVEL
# print(cores_tuple)