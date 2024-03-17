#Functions (Funções)
    #DRY - Don't Repeat Yourself.
    
def boas_vindas(nome, quantidade):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} notebooks em estoque')
    
boas_vindas('Lucas', 8)
boas_vindas('Rodrigo', 6)
boas_vindas('Emily', 3)