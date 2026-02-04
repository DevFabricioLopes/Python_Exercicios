# pede para o usuário digitar o tamanho da primeira reta
r1 = int(input('Digite o tamanho da reta 1: '))

# pede para o usuário digitar o tamanho da segunda reta
r2 = int(input('Digite o tamanho da reta 2: '))

# pede para o usuário digitar o tamanho da terceira reta
r3 = int(input('Digite o tamanho da reta 3: '))

# aqui o programa verifica a regra do triângulo:
# cada reta precisa ser MENOR que a soma das outras duas
# se TODAS essas condições forem verdadeiras, forma triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    
    # se entrou aqui, as três retas conseguem formar um triângulo
    print('Forma um triângulo')

else:
    # se entrou aqui, pelo menos uma das condições foi falsa
    # então não é possível formar um triângulo
    print('Não forma triângulo')
