# Lê o primeiro número digitado pelo usuário e converte para inteiro
n1 = int(input('Digite o número 1: '))

# Lê o segundo número digitado pelo usuário e converte para inteiro
n2 = int(input('Digite o número 2: '))

# Lê o terceiro número digitado pelo usuário e converte para inteiro
n3 = int(input('Digite o número 3: '))

# Verifica se o primeiro número é maior que o segundo e o terceiro
# (aqui estava o erro: você comparou n1 > n2 duas vezes)
if n1 > n2 and n1 > n3:
    print(f'O número {n1} é o maior')

# Se o primeiro não for o maior, verifica se o segundo é maior que os outros dois
elif n2 > n1 and n2 > n3:
    print(f'O número {n2} é o maior')

# Se nenhuma das condições acima for verdadeira,
# então o terceiro número é o maior
else:
    print(f'O número {n3} é o maior')
