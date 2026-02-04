# Programa que calcula desconto na conta de luz
# com base no valor da fatura

# Entrada do valor da conta de luz
luz = float(input('Digite o valor da conta de luz: R$ '))

# Verifica a faixa de valor para aplicar desconto
if luz > 250:
    # Desconto de 5% para contas acima de R$250
    desconto = luz * 0.05
    valor_final = luz - desconto
    print('Desconto aplicado: 5%')

elif 150 <= luz <= 250:
    # Desconto de 3% para contas entre R$150 e R$250
    desconto = luz * 0.03
    valor_final = luz - desconto
    print('Desconto aplicado: 3%')

else:
    # Contas abaixo de R$150 não têm desconto
    desconto = 0
    valor_final = luz
    print('Esta conta não possui desconto.')

# Exibe o resumo final
print(f'Valor original da conta: R${luz:.2f}')
print(f'Desconto: R${desconto:.2f}')
print(f'Valor final a pagar: R${valor_final:.2f}')
