# Programa que calcula descontos diferentes de acordo
# com a forma de pagamento escolhida pelo cliente

# Solicita o valor do produto
produto = float(input('Digite o valor do produto: R$ '))

# Calcula desconto de 5% para pagamento à vista
desconto_avista = produto * 0.05
valor_avista = produto - desconto_avista

# Calcula desconto de 8% para pagamento em dinheiro
desconto_dinheiro = produto * 0.08
valor_dinheiro = produto - desconto_dinheiro

# Exibe os resultados
print('\nResumo dos descontos:')
print(f'Pagamento à vista (5% de desconto): R$ {valor_avista:.2f}')
print(f'Pagamento em dinheiro (8% de desconto): R$ {valor_dinheiro:.2f}')
