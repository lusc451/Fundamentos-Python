#Python Object-Oriented Programming

#Classes
    #Utilizadas para criar Objetos (instances)
    #Objetos são partes dentro de uma Class (instancias)
    #Classes são utilizadas para agrupar dados e funções, podendo reutilizar
    #===
    #Class: Frutas
    #Objects: Abacate, Banana...
  
#CRIAR A CLASSE  
class Funcionarios:
    
    def __init__(self, nome, sobrenome, data_nasc):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nasc = data_nasc
        

#CRIAR O OBJETO
usuario1 = Funcionarios('Lucas', 'Antunes', '23/04/1999')
usuario2 = Funcionarios('Rodrigo', 'Marques', '15/02/1960')

#EXIBIR DADOS
print(usuario1.nome)
print(usuario2.nome)


# #CRIAR OS PARAMETROS DO USUÁRIO1
# usuario1.nome = 'Lucas'
# usuario1.sobrenome = 'Antunes'
# usuario1.data_nasc = '23/04/1999'

# #CRIAR OS PARAMETROS DO USUÁRIO2
# usuario2.nome = 'Rodrigo'
# usuario2.sobrenome = 'Marques'
# usuario2.data_nasc = '15/02/1960'
