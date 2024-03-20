#Lambda Function
    #É uma função (pequena) sem nome
    #Pode ter vários argumentos mas somente 1 expressão
    #Muito utilizada dentro de outras funções
    #Código mais "Clean"

# def somar(x):  função completa
#     return x + 10
# print(somar(2))


somar10 = lambda x, y: x + y + 10 #Função Lambda - executa a mesma tarefa que a função completa, porém, em menos linhas
print(somar10(2, 3))