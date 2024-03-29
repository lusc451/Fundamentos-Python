#Desafio com If, Elif, Else

'''
Criar um programa que dependendo da temperatura (em celsius) do steak
ele retorna o ponto de cozimento em português. O usuário deverá
fornecer a temperatura.

Temperatura - Cozimento
120ºF ou 48ºC - Rare (Selada)
130ºF ou 54ºC - Medium Rare (Ao ponto para o mal)
140ºF ou 60ºC - Medium (Ao ponto)
150ºF ou 65ºC - Medium Well (Ao ponto para o bem)
160ºF ou 71ºC - Well Done (Bem passada)
'''

temp = int(input('Digite a temperatura da carne: '))

# if temp < 48:
#     ponto = 'Deixe a carne cozinhar por mais alguns minutos.'

# elif 48 <= temp <= 53:
#     ponto = 'Carne selada'

# elif 54 <= temp <= 59:
#     ponto = 'Carne ao ponto para o mal'

# elif 60 <= temp <= 64:
#     ponto = 'Carne ao ponto'
    
# elif 65 <= temp <= 70:
#     ponto = 'Carne ao ponto para o bem'
# else: ponto = 'Carne bem passada'

#Resolução utilizando range no IF
if temp < 48:
    ponto = 'Deixe a carne cozinhar por mais alguns minutos.'
elif temp in range(48, 53):
    ponto = 'Carne selada'
elif temp in range(54, 59):
    ponto = 'Carne ao ponto para o mal'
elif temp in range(60, 64):
    ponto = 'Carne ao ponto'
elif temp in range(65, 70):
    ponto = 'Carne ao ponto para o bem'
elif temp >= 71:
    ponto = 'Carne bem passada'

print(ponto)