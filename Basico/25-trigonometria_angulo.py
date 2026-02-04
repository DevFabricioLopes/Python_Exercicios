# Programa que calcula seno, cosseno e tangente de um ângulo
# O ângulo é informado em graus e convertido para radianos

# Importa o módulo math para funções trigonométricas
import math

# Entrada do ângulo em graus
angulo_graus = int(input(
    'Digite um ângulo em graus para calcular seno, cosseno e tangente: '
))

# Converte o ângulo de graus para radianos
angulo_radianos = math.radians(angulo_graus)

# Calcula seno, cosseno e tangente do ângulo
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

# Exibe os resultados
print(f'Ângulo em radianos: {angulo_radianos:.2f}')
print(f'Seno: {seno:.2f}')
print(f'Cosseno: {cosseno:.2f}')
print(f'Tangente: {tangente:.2f}')
