from datetime import datetime

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
    
    def __init__(self, nome, sobrenome, ano_nasc):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nasc = ano_nasc
        
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nasc = int(ano_atual - self.ano_nasc)
        return self.ano_nasc
        

#CRIAR O OBJETO
usuario1 = Funcionarios('Lucas', 'Antunes', 1999)
usuario2 = Funcionarios('Rodrigo', 'Marques', 1960)

#EXIBIR DADOS
print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.idade_funcionario(usuario2))