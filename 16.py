produto = float(input('Digite o valor do produto: '))

desconto = produto * 0.07
novo_desconto = produto - desconto

acrescimo = produto * 0.12
novo_acrescimo = produto + acrescimo

print(f'O valor à vista com desconto é: R${novo_desconto:.2f}')
print(f'O valor parcelado com acréscimo é: R${novo_acrescimo:.2f}')
