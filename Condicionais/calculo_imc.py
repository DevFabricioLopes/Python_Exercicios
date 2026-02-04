
# Programa que calcula o IMC (Índice de Massa Corporal)
# e informa a classificação da pessoa

# Entrada do peso em kg
peso = float(input('Digite seu peso (kg): '))

# Entrada da altura em metros
altura = float(input('Digite sua altura (m): '))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibe o valor do IMC calculado
print(f'Seu IMC é: {imc:.2f}')

# Classificação do IMC
if imc < 18.5:
    print('Classificação: Abaixo do peso')

elif 18.5 <= imc <= 24.9:
    print('Classificação: Peso normal')

elif 25 <= imc <= 29.9:
    print('Classificação: Sobrepeso')

else:
    print('Classificação: Obesidade')
