# Solicita o valor normal do produto
preco_normal = float(input('Qual o valor do produto? '))

# Solicita a forma de pagamento
print('FORMAS DE PAGAMENTO')
print('[1] À vista em dinheiro/cheque (10% de desconto)')
print('[2] À vista no cartão (5% de desconto)')
print('[3] Cartão em até 2x (preço normal)')
print('[4] Cartão em 3x ou mais (20% de juros)')

forma_pagamento = int(input('Digite a forma de pagamento: '))

# Calcula os valores finais
dinheiro = preco_normal - (preco_normal * 0.10)
avista_cartao = preco_normal - (preco_normal * 0.05)
cartao_2x = preco_normal
cartao_3x = preco_normal + (preco_normal * 0.20)

# Verifica a forma de pagamento escolhida
if forma_pagamento == 1:
    print(f'O preço normal é R$ {preco_normal:.2f}')
    print(f'Pagando à vista em dinheiro, o valor fica R$ {dinheiro:.2f}')

elif forma_pagamento == 2:
    print(f'O preço normal é R$ {preco_normal:.2f}')
    print(f'Pagando à vista no cartão, o valor fica R$ {avista_cartao:.2f}')

elif forma_pagamento == 3:
    print(f'O preço do produto é R$ {preco_normal:.2f}')
    print(f'Pagamento em até 2x no cartão, valor final R$ {cartao_2x:.2f}')

elif forma_pagamento == 4:
    print(f'O preço do produto é R$ {preco_normal:.2f}')
    print(f'Pagamento em 3x ou mais no cartão, com juros, o valor fica R$ {cartao_3x:.2f}')

else:
    print('Forma de pagamento inválida!')
