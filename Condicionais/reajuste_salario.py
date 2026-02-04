# Programa que calcula o reajuste salarial
# de acordo com o valor do salário informado

# Solicita o salário atual do funcionário
salario = float(input('Digite o valor do salário: R$ '))

# Verifica se o salário é até 3000
if salario <= 3000:
    # Calcula aumento de 12%
    aumento = salario * 0.12
    novo_salario = salario + aumento

    # Exibe o resultado
    print(f'Seu aumento foi de R$ {aumento:.2f}')
    print(f'Seu novo salário é de R$ {novo_salario:.2f}')

# Caso o salário seja maior que 3000
elif salario > 3000:
    # Calcula aumento de 8%
    aumento = salario * 0.08
    novo_salario = salario + aumento

    # Exibe o resultado
    print(f'Seu aumento foi de R$ {aumento:.2f}')
    print(f'Seu novo salário é de R$ {novo_salario:.2f}')
