# Pede ao usuário que digite um número
# input() retorna texto, então usamos int() para converter para número inteiro
num = int(input('Digite um número: '))

# Laço for que vai repetir 10 vezes
# range(1, 11) gera os números de 1 até 10
for contador in range(1, 11):

    # Calcula o resultado da multiplicação
    # contador muda a cada volta do laço
    resultado = contador * num

    # Mostra o cálculo da tabuada na tela
    # Exemplo: 3 x 5 = 15
    print(f'{contador} x {num} = {resultado}')
