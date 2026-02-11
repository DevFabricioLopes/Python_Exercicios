# Mostra o menu de opções para o usuário
print('MENU')
print('[1] Verificar o sinal do número')
print('[2] Verificar par ou ímpar')
print('[3] Maior de 3 números')

# Lê a opção escolhida pelo usuário e converte para inteiro
opcao = int(input('Escolha uma opção: '))

# =========================
# OPÇÃO 1 – SINAL DO NÚMERO
# =========================
if opcao == 1:
    # Pede um número ao usuário
    n = int(input('Digite um número: '))

    # Verifica se o número é negativo
    if n < 0:
        print('O número é negativo')

    # Verifica se o número é zero
    elif n == 0:
        print('O número é igual a zero')

    # Caso não seja negativo nem zero, é positivo
    else:
        print('O número é positivo')

# =========================
# OPÇÃO 2 – PAR OU ÍMPAR
# =========================
elif opcao == 2:
    # Pede um número ao usuário
    n = int(input('Digite um número: '))

    # Se o resto da divisão por 2 for zero, o número é par
    if n % 2 == 0:
        print('O número é par')

    # Caso contrário, o número é ímpar
    else:
        print('O número é ímpar')

# =========================
# OPÇÃO 3 – MAIOR DE 3 NÚMEROS
# =========================
elif opcao == 3:
    # Pede três números ao usuário
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    n3 = int(input('Digite o terceiro número: '))

    # Verifica se os três números são iguais
    if n1 == n2 == n3:
        print('Todos os números são iguais')

    # Verifica se o primeiro número é o maior
    elif n1 > n2 and n1 > n3:
        print(f'O maior é {n1}')

    # Verifica se o segundo número é o maior
    elif n2 > n1 and n2 > n3:
        print(f'O maior é {n2}')

    # Verifica se o terceiro número é o maior
    elif n3 > n1 and n3 > n2:
        print(f'O maior é {n3}')

    # Caso sobre empate entre dois números
    else:
        print('Há empate entre dois números')

# =========================
# OPÇÃO INVÁLIDA
# =========================
else:
    # Executa se o usuário digitar uma opção que não existe
    print('Opção inválida')
