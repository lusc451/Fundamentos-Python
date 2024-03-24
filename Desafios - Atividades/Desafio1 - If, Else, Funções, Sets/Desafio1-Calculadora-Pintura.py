#Desafio com funções

'''
Criar um programa que calcula a quantidade de tinta necessária para
pintar uma parede. O usuário deverá fornecer as seguintes
informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tinta'
'''

# import math

rendimento = float(input('Qual o rendimento da lata? '))
altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))

def latas(altura, largura, rendimento):
    area_parede = altura * largura
    return area_parede / rendimento

qtd_latas = latas(altura, largura, rendimento)

print(f'Voce precisa de {qtd_latas} latas de tinta')