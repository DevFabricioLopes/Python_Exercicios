valor_casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o valor do seu salário? '))
anos = int(input('Quantos anos pretende pagar a casa? '))

prestacao = valor_casa / (anos * 12)
limite = salario * 0.30

if prestacao > limite:
    print(
        f'Para pagar uma casa de R$ {valor_casa:.2f} '
        f'em {anos} anos, a prestação será de R$ {prestacao:.2f}. '
        f'Empréstimo NEGADO!'
    )
else:
    print(
        f'Para pagar uma casa de R$ {valor_casa:.2f} '
        f'em {anos} anos, a prestação será de R$ {prestacao:.2f}. '
        f'Empréstimo APROVADO!'
    )
