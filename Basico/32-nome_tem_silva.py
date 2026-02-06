# Programa que verifica se o nome da pessoa contém "Silva"

nome = input('Digite seu nome: ').strip()

# Converte o nome para minúsculas e verifica se contém "silva"
tem_silva = 'silva' in nome.lower()

# Exibe o resultado
print(f'Seu nome tem Silva? {tem_silva}')
