# Lê o primeiro lado do triângulo
a = int(input('Lado 1: '))

# Lê o segundo lado do triângulo
b = int(input('Lado 2: '))

# Lê o terceiro lado do triângulo
c = int(input('Lado 3: '))

# Verifica se é possível formar um triângulo
# A soma de dois lados deve ser maior que o terceiro
if a + b > c and a + c > b and b + c > a:
    print('Forma um triângulo')

    # Se todos os lados forem iguais
    if a == b == c:
        print('Equilátero')

    # Se pelo menos dois lados forem iguais
    elif a == b or a == c or b == c:
        print('Isósceles')

    # Se todos os lados forem diferentes
    else:
        print('Escaleno')

# Caso não seja possível formar um triângulo
else:
    print('Não forma um triângulo')
