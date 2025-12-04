# crie um programa  que leia o nome completo de uma pessoa e mostre: 
#o nome com todas as letras maiusculas: 
#o nome com todas as letras minusculas: 
#quantas letras ao todo (sem considerar espaços)
#quantas letras tem o primeiro nome



frase = input('Qual seu nome? ')

print(f'O nome maiúsculo é: {frase.upper()}')
print(f'O nome minúsculo é: {frase.lower()}')
print(f' o nome  tem :  {len(frase.strip())} letras    ')

primeiro_nome = frase.split()[0]

print(f'O primeiro nome é: {primeiro_nome}')
print(f'O primeiro nome tem {len(primeiro_nome)} letras')
