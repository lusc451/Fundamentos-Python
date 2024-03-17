#Functions (Funções)
    #DRY - Don't Repeat Yourself.
    #Parametro --> Argumento
    #Default = Aquele que você define o valor no parametro
    #Non-Default = Aquele que você não define o valor no parametro
    
#PARAMETRO NON-DEFAULT NECESSÁRIAMENTE TEM QUE SER O ULTIMO PARAMETRO NA FUNÇÃO
def boas_vindas(nome, quantidade=6):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} notebooks em estoque')
    
boas_vindas('Lucas', 8)
boas_vindas('Rodrigo')
boas_vindas('Emily')