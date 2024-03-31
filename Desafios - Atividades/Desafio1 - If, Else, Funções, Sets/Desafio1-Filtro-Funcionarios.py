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

lista1 = set(funcionarios)
lista2 = set(turno_dia)
lista3 = set(tem_carro)

print(lista1 - lista2 & lista3)
print(lista1 & lista2 & lista3)