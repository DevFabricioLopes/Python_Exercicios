# Programa que calcula o valor final de um produto
# considerando duas formas de pagamento:
# - À vista com desconto
# - Parcelado com acréscimo

# Solicita ao usuário o valor original do produto
produto = float(input('Digite o valor do produto: R$ '))

# Calcula o desconto de 7% para pagamento à vista
desconto = produto * 0.07
valor_avista = produto - desconto

# Calcula o acréscimo de 12% para pagamento parcelado
acrescimo = produto * 0.12
valor_parcelado = produto + acrescimo

# Exibe os resultados formatados
print('\nResumo de pagamento:')
print(f'Valor original do produto: R$ {produto:.2f}')
print(f'Pagamento à vista (7% de desconto): R$ {valor_avista:.2f}')
print(f'Pagamento parcelado (12% de acréscimo): R$ {valor_parcelado:.2f}')
