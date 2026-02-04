# Programa que calcula o valor final de um produto
# de acordo com o número de parcelas escolhidas

# Solicita o valor do produto
produto = float(input('Digite o valor do produto: R$ '))

# Calcula o acréscimo de 8% para pagamento em 3x
acrescimo_3x = produto * 0.08
valor_total_3x = produto + acrescimo_3x
valor_parcela_3x = valor_total_3x / 3

# Calcula o acréscimo de 16% para pagamento em 6x
acrescimo_6x = produto * 0.16
valor_total_6x = produto + acrescimo_6x
valor_parcela_6x = valor_total_6x / 6

# Exibe os resultados
print('\nResumo do parcelamento:')
print(f'3x com acréscimo de 8%:')
print(f'Valor total: R$ {valor_total_3x:.2f}')
print(f'Valor de cada parcela: R$ {valor_parcela_3x:.2f}')

print('\n6x com acréscimo de 16%:')
print(f'Valor total: R$ {valor_total_6x:.2f}')
print(f'Valor de cada parcela: R$ {valor_parcela_6x:.2f}')
