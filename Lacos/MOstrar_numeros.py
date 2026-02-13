# Mostra todos os números de 1 até o número digitado
# Comentário explicando o objetivo do programa

# Solicita que o usuário digite um número
# input() retorna string, por isso usamos int() para converter para inteiro
numero = int(input('Digite um número: '))

# Loop que vai de 1 até o número digitado
# range(1, numero + 1) começa em 1
# O +1 é necessário porque o limite final do range não é incluído
for contador in range(1, numero + 1):

    # Imprime o número atual da contagem
    print(contador)
