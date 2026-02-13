# Laço de repetição for
# Indica que será usado um loop para repetir uma ação várias vezes

# range(0, 51, 2)
# 0 → valor inicial (começa no zero)
# 51 → limite final (não incluso, então vai até 50)
# 2 → passo (incrementa de 2 em 2)
# Isso faz com que apenas números pares sejam gerados
for c in range(0, 51, 2):

    # Exibe na tela o número atual da repetição
    # A variável 'c' recebe cada valor gerado pelo range
    # A f-string permite inserir o valor de 'c' dentro da frase
    print(f'O número par é: {c}')
