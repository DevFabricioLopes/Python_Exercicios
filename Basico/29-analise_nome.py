# crie um programa  que leia o nome completo de uma pessoa e mostre: 
#o nome com todas as letras maiusculas: 
#o nome com todas as letras minusculas: 
#quantas letras ao todo (sem considerar espaços)
#quantas letras tem o primeiro nome



# Programa que analisa o nome completo de uma pessoa

# Entrada do nome completo
nome = input('Digite seu nome completo: ').strip()

# Mostra o nome em letras maiúsculas
print(f'Nome em maiúsculas: {nome.upper()}')

# Mostra o nome em letras minúsculas
print(f'Nome em minúsculas: {nome.lower()}')

# Conta o total de letras sem considerar os espaços
total_letras = len(nome.replace(' ', ''))
print(f'Total de letras (sem espaços): {total_letras}')

# Separa o primeiro nome
primeiro_nome = nome.split()[0]

# Exibe informações do primeiro nome
print(f'Primeiro nome: {primeiro_nome}')
print(f'Quantidade de letras do primeiro nome: {len(primeiro_nome)}')




      
        
