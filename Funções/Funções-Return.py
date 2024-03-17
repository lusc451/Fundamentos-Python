#Functions (Funções)
    #DRY - Don't Repeat Yourself.
    #Realizam uma tarefa
    #Calcula um valor
    
def cliente1(nome):
    print(f'Olá {nome}.')
    

def cliente2(nome):
    return f'Olá {nome}.'

x = cliente1('Maria')
y = cliente2('José')

print(x)
print(y)