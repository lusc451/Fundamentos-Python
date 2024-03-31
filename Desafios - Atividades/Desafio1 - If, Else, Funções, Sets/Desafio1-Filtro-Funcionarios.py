#Desafio com 'Sets'

'''
Criar um programa que gere 3 listas de acordo com a necessidade logo abaixo:

Lista 1 = Funcionários que tem carro e trabalham a noite
Lista 2 = Funcionários que tem carro e trabalham durante o dia
Lista 3 = Funcionários que não tem carro
'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

# lista1 = set(funcionarios)
# lista2 = set(turno_dia)
# lista3 = set(tem_carro)

#print(lista1 - lista2 & lista3) #Funcionários que tem carro e trabalham a noite
#print(lista1 & lista2 & lista3) #Funcionários que tem carro e trabalham durante o dia
#print(lista1 - lista3) #Funcionários que não tem carro

#RESOLUÇÃO

#LISTA 1
lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

#LISTA 2
lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

#LISTA 3
lista3 = set(funcionarios).difference(tem_carro)
print(lista3)