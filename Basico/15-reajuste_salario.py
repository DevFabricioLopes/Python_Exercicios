# Programa que calcula o novo salário de um funcionário
# considerando faixas diferentes de aumento

# Solicita o salário atual do funcionário
salario = float(input('Digite o valor do salário: R$ '))

# Verifica a faixa salarial para definir o percentual de aumento
if salario <= 1500:
    percentual = 0.20  # 20% de aumento
else:
    percentual = 0.10  # 10% de aumento

# Calcula o valor do aumento
aumento = salario * percentual

# Calcula o novo salário
novo_salario = salario + aumento

# Exibe o resultado de forma clara e formatada
print(f'Salário atual: R$ {salario:.2f}')
print(f'Aumento aplicado: {percentual * 100:.0f}%')
print(f'Valor do aumento: R$ {aumento:.2f}')
print(f'Novo salário: R$ {novo_salario:.2f}')
