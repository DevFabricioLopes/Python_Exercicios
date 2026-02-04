# Lê o nome do usuário e remove espaços extras
nome = input('Digite seu nome: ').strip()

# Divide o nome em uma lista de palavras
nome = nome.split()

# Mostra o primeiro nome
print(f'Seu primeiro nome é: {nome[0]}')

# Mostra o último nome
print(f'Seu último nome é: {nome[-1]}')
