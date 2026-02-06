# Pede ao usuário para digitar um número inteiro
# input() retorna uma string, então usamos int() para converter para inteiro
num = int(input('Digite um numero inteiro: '))

# Pede ao usuário que escolha a base de conversão
# 1 = binário, 2 = octal, 3 = hexadecimal
base = int(input(
    'Qual base vc quer a conversao: Digite 1 para binario; 2 para converter em octal e 3 para converter em dexadecimal: '))

# Verifica se a base escolhida foi 1
if base == 1:
    # Se for 1, informa que a conversão será para binário
    print('A base da conversao sera binario')

# Verifica se a base escolhida foi 2
elif base == 2:
    # Se for 2, informa que a conversão será para octal
    print('A conversao sera octal')

# Caso não seja 1 nem 2 (ou seja, 3 ou qualquer outro valor)
else:
    # Informa que a conversão será para hexadecimal
    print('A base da conversao é dexadecimal')
