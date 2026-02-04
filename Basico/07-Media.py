# Solicita ao usuário a primeira nota
# O valor digitado é convertido para float para permitir notas decimais
n1 = float(input('Digite a nota 1: '))

# Solicita ao usuário a segunda nota
# Também convertida para float
n2 = float(input('Digite a nota 2: '))

# Calcula a média aritmética das duas notas
media = (n1 + n2) / 2

# Exibe o resultado da média
print(f'A média é: {media}')
