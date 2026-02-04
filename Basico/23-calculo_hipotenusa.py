# Programa que calcula a hipotenusa de um triângulo retângulo
# usando o Teorema de Pitágoras

# Importa o módulo math para usar a função sqrt (raiz quadrada)
import math

# Entrada dos valores dos catetos
oposto = float(input('Digite o cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))

# Aplica o Teorema de Pitágoras:
# hipotenusa² = cateto_oposto² + cateto_adjacente²
hipotenusa_quadrado = (oposto ** 2) + (adjacente ** 2)

# Calcula a raiz quadrada para obter a hipotenusa
hipotenusa = math.sqrt(hipotenusa_quadrado)

# Exibe o resultado formatado
print(f'A hipotenusa vai medir: {hipotenusa:.2f}')
