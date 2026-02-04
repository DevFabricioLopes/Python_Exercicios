# Programa para calcular o salário mensal de um trabalhador

# Solicita a quantidade de horas trabalhadas no mês
# Usamos float para permitir valores decimais
horas_trabalhadas = float(input('Digite o total de horas trabalhadas no mês: '))

# Solicita o valor recebido por hora de trabalho
valor_hora = float(input('Digite o valor recebido por hora: R$ '))

# Calcula o salário bruto
salario_bruto = horas_trabalhadas * valor_hora

# Calcula o desconto do INSS (8%)
desconto_inss = salario_bruto * 0.08

# Calcula o salário líquido
salario_liquido = salario_bruto - desconto_inss

# Exibe os resultados
print('\n💰 Demonstrativo de salário')
print(f'Salário bruto: R$ {salario_bruto:.2f}')
print(f'Desconto INSS (8%): R$ {desconto_inss:.2f}')
print(f'Salário líquido: R$ {salario_liquido:.2f}')
