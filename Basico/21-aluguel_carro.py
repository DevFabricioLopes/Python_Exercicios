# Programa que calcula o valor total do aluguel de um carro
# com base nos dias alugados e quilômetros rodados

# Entrada da quantidade de dias alugados
dias = int(input('Quantos dias alugados? '))

# Entrada da quantidade de quilômetros rodados
km = float(input('Quantos km rodados? '))

# Valores fixos do aluguel
valor_dia = 60        # custo por dia alugado
valor_km = 0.15       # custo por km rodado

# Cálculo do valor total
total = (dias * valor_dia) + (km * valor_km)

# Exibe o valor total a pagar
print(f'O total a pagar é: R${total:.2f}')
