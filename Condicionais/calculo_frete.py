# Programa que calcula o valor do frete com base
# no valor da compra e na distância em km

# Entrada do valor da compra
valor = int(input('Digite o valor da compra: R$ '))

# Entrada da distância em quilômetros
km = float(input('Digite a distância em km: '))

# Verifica as condições para o frete
if valor >= 300:
    # Compras a partir de R$300 têm frete grátis
    frete = 0
    print('O frete é grátis.')

elif valor < 300 and km <= 50:
    # Compras abaixo de R$300 e até 50 km
    frete = 20
    print('O frete custa R$20,00.')

else:
    # Compras abaixo de R$300 e acima de 50 km
    frete = 35
    print('O frete custa R$35,00.')

# Exibe o valor final da compra
print(f'Valor da compra: R${valor}')
print(f'Valor do frete: R${frete}')
print(f'Valor total a pagar: R${valor + frete}')
