#Dicionarios
    #Utiliza index no formato de Keys e Values
    #Aceita string, integer, float, boolean...
    
alunos = {'nome': 'Lucas', 'idade': 25, 'nota final': '10', 'aprovação': True}

for keys, values in alunos.items():
    print(keys, ':', values)