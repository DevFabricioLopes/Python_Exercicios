# pede para a pessoa digitar o salário
salario = float(input('Qual valor do seu salário: '))

# aqui o programa pergunta:
# "o salário é MAIOR que 1250?"
if salario > 1250:
    
    # se entrou aqui, então o salário é maior que 1250
    # calcula 10% do salário (divide por 100 e multiplica por 10)
    aumento = salario * 0.10
    
    # soma o aumento com o salário antigo
    novo_salario = salario + aumento
    
    # mostra tudo na tela
    print(f'Seu salário é de R$ {salario:.2f} e você recebeu 10% de aumento, ficando em R$ {novo_salario:.2f}')

else:
    # se entrou aqui, é porque NÃO é maior que 1250
    # ou seja: é menor OU igual a 1250
    
    # calcula 15% de aumento
    aumento = salario * 0.15
    
    # soma o aumento com o salário antigo
    novo_salario = salario + aumento
    
    # mostra o resultado
    print(f'Seu salário é de R$ {salario:.2f} e você recebeu 15% de aumento, ficando em R$ {novo_salario:.2f}')
