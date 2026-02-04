# Simulação de um caixa eletrônico
# O programa calcula a quantidade de cédulas necessárias
# para um determinado valor de saque

# Solicita o valor do saque
valor = int(input('Digite o valor do saque: R$ '))

# Verifica se o valor é válido
if valor <= 0:
    print('Valor inválido. Digite um valor maior que zero.')
else:
    # Variáveis para armazenar a quantidade de cédulas
    cedulas_50 = valor // 50
    valor %= 50

    cedulas_20 = valor // 20
    valor %= 20

    cedulas_10 = valor // 10
    valor %= 10

    cedulas_1 = valor // 1

    # Exibe o resultado
    print('\n💵 Cédulas entregues:')
    print(f'R$50: {cedulas_50}')
    print(f'R$20: {cedulas_20}')
    print(f'R$10: {cedulas_10}')
    print(f'R$1: {cedulas_1}')
