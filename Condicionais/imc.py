# Solicita a altura do usuário em metros
# Usa float porque a altura pode ter casas decimais (ex: 1.75)
alt = float(input('Qual sua altura? '))

# Solicita o peso do usuário em quilogramas
# Usa float porque o peso também pode ter casas decimais
peso = float(input('Qual seu peso? '))

# Calcula o IMC (Índice de Massa Corporal)
# Fórmula: peso dividido pela altura ao quadrado
imc = peso / (alt * alt)

# Verifica se o IMC é menor que 18.5
if imc < 18.5:
    # Abaixo do peso
    print('Você está abaixo do peso')

# Verifica se o IMC está entre 18.5 e 24.9
elif imc >= 18.5 and imc < 25:
    # Peso ideal
    print('Você está no peso ideal')

# Verifica se o IMC está entre 25 e 29.9
elif imc >= 25 and imc < 30:
    # Sobrepeso
    print('Você está com sobrepeso')

# Verifica se o IMC está entre 30 e 39.9
elif imc >= 30 and imc < 40:
    # Obesidade
    print('Você está obeso')

# Caso o IMC seja 40 ou maior
else:
    # Obesidade mórbida
    print('Obesidade mórbida')





