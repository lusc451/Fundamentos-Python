
#Dicionarios
    #Utiliza index no formato de Keys e Values
    #Aceita string, integer, float, boolean...
    
alunos = {'nome': 'Lucas', 'idade': 25, 'nota final': '10', 'aprovação': True}

#ATUALIZAR DADOS NO DICIONARIO

# alunos['nome'] = 'João'
# alunos.update({'nome': 'Rodrigo', 'nota final': '8'})
# alunos.update({'endereço': 'Rua A'})
del alunos['idade']

print(alunos)
# print(alunos.get('endereço', 'Não existe o campo endereço'))