# Solicita ao usuário o valor total da casa e converte para número decimal
valor_casa = float(input('Qual é o valor da casa?: '))

# Solicita o salário do comprador e converte para número decimal
salario = float(input('Qual é o seu salário?: '))

# Solicita em quantos anos o empréstimo será pago
anos = float(input('Quantos anos você vai pagar o empréstimo?: '))

# Calcula a prestação mensal
# anos * 12 converte o tempo de pagamento de anos para meses
prestacao = valor_casa / (anos * 12)

# Verifica se a prestação mensal ultrapassa 30% do salário
if prestacao > 0.30 * salario:
    # Se ultrapassar, o financiamento é negado
    print('Financiamento negado')
else:
    # Caso contrário, o financiamento é aprovado
    print('Financiamento aprovado')
