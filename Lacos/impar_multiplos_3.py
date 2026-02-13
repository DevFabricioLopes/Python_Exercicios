# Loop que percorre números de 0 até 500
# range(0, 501) começa no 0 e vai até 500
# O 501 não é incluído (o limite final do range é sempre exclusivo)
for c in range(0, 501):

    # Verifica duas condições ao mesmo tempo:
    # 1) Se o número é múltiplo de 3 (resto da divisão por 3 é 0)
    # 2) Se o número é ímpar (resto da divisão por 2 é 1)
    # O operador "and" exige que as duas condições sejam verdadeiras
    if c % 3 == 0 and c % 2 == 1:

        # Exibe na tela o número que atende às duas condições
        # A f-string permite inserir o valor da variável {c} dentro da frase
        print(c)
