#Calculo de IMC - Índice de Massa Corporal

'''
Qual é a sua altura em cm:
Qual é o seu peso em kg:
'''

# MENOR QUE 18,5 -- MAGREZA
# ENTRE 18,5 E 24,9 -- NORMAL
# ENTRE 25,0 E 29,9 -- SOBREPESO
# ENTRE 30,0 E 39,9 -- OBESIDADE
# MAIOR QUE 40,0 -- OBESIDADE GRAVE

peso = float(input('Qual é o seu peso em kg: '))
altura = float(input('Qual é a sua altura em cm: '))

altura_m = altura / 100  # Convertendo altura para metros
imc = peso / (altura_m ** 2)

if imc < 18.5:
    categoria = "Magreza"
elif 18.5 <= imc < 24.9:
    categoria = "Normal"
elif 25 <= imc < 29.9:
    categoria = "Sobrepeso"
elif 30 <= imc < 39.9:
    categoria = "Obesidade"
elif imc > 40:
    categoria = "Obesidade Grave"
    
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {categoria}")