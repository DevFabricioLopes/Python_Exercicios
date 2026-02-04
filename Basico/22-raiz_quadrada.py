# Programa que calcula a raiz quadrada de um número
# utilizando a biblioteca math

# Importa apenas a função sqrt (raiz quadrada) do módulo math
from math import sqrt

# Solicita um número inteiro ao usuário
num = int(input('Digite um número: '))

# Calcula a raiz quadrada do número
raiz = sqrt(num)

# Exibe o resultado formatado
print(f'A raiz quadrada de {num} é igual a {raiz:.2f}')
