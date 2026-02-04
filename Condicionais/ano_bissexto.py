# Pede ao usuário que digite um ano
# int() é mais adequado, pois ano não usa casas decimais
ano = int(input('Digite o ano: '))

# Verifica se o ano é divisível por 4
# Se o resto da divisão por 4 for 0, o ano é bissexto
if ano % 4 == 0:
    print('É um ano bissexto')
else:
    print('Não é um ano bissexto')
