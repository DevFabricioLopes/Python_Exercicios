# Solicita ao usuário que digite o primeiro número
# O input() retorna texto, então usamos int() para converter para número inteiro
n1 = int(input('Digite o primeiro numero: '))

# Solicita ao usuário que digite o segundo número
n2 = int(input('Digite o segundo numero: '))

# Verifica se o primeiro número é maior que o segundo
if n1 > n2:
    # Se n1 for maior, mostra uma mensagem informando isso
    print(f'O numero {n1} é maior')

# Caso a condição anterior seja falsa, verifica se o segundo número é maior
elif n2 > n1:
    # Se n2 for maior, mostra uma mensagem informando isso
    print(f'O numero {n2} é maior')

# Se nenhuma das condições anteriores for verdadeira,
# significa que os dois números são iguais
else:
    # Exibe uma mensagem informando que os números são iguais
    print(f'Os numeros {n1} e {n2} sao iguais')
