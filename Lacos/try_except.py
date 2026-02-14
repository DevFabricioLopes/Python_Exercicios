# Programa que verifica se um número é par ou ímpar
# e trata erro caso o usuário não digite um número

try:
    # Pede para o usuário digitar um número
    num = int(input('Digite um número: '))
    
    # Mostra o número digitado
    print(f'Você digitou o número {num}')

    # Verifica se o número é par
    if num % 2 == 0:
        print('O número é par')
    else:
        # Se não for par, é ímpar
        print('O número é ímpar')

# Se o usuário digitar algo que não é número
except ValueError:
    print('Você não digitou um número válido.')
