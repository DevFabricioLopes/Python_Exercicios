# Solicita ao usuário um valor em dólares
# O valor digitado é convertido para float para permitir casas decimais
dolar = float(input('Digite o valor em dólares: '))

# Converte o valor de dólares para euros
# Taxa de conversão utilizada: 1 dólar = 0.75 euro
euro = dolar * 0.75

# Exibe o resultado da conversão
# :.2f limita o valor para duas casas decimais
print(f'Com {dolar} dólares você pode comprar {euro:.2f} euros')
