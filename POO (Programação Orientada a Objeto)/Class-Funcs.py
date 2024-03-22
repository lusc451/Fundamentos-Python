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
        
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

#CRIAR O OBJETO
usuario1 = Funcionarios('Lucas', 'Antunes', '23/04/1999')
usuario2 = Funcionarios('Rodrigo', 'Marques', '15/02/1960')

#EXIBIR DADOS
# print(usuario1.nome)
# print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1))