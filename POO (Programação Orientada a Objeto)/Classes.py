#Python Object-Oriented Programming

#Classes
    #Utilizadas para criar Objetos (instances)
    #Objetos são partes dentro de uma Class (instancias)
    #Classes são utilizadas para agrupar dados e funções, podendo reutilizar
    #===
    #Class: Frutas
    #Objects: Abacate, Banana...
    
class Funcionarios:
    nome = 'Lucas'
    sobrenome = 'Antunes'
    data_nasc = '23/04/1999'

usuario1 = Funcionarios()
print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nasc)

#TESTE DE ARMAZENAMENTO E EXIBIÇÃO DE DADOS EM UMA CLASSE E OBJETO