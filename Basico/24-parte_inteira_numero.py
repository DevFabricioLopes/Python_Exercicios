# Programa que mostra apenas a parte inteira de um número real

# Importa o módulo math para usar funções matemáticas
import math

# Solicita um número real (float) ao usuário
num = float(input('Digite um número real: '))

# Remove a parte decimal do número usando a função trunc()
inteiro = math.trunc(num)

# Exibe o número sem a parte decimal
print(f'O número com a porção inteira é: {inteiro}')
