# Programa que calcula duas promoções diferentes
# para o valor de um celular e mostra os preços finais

# Solicita o valor do celular ao usuário
celular = float(input('Digite o valor do celular: R$ '))

# Promoção A: desconto de 10%
promocao_a = celular * 0.10
final_a = celular - promocao_a

# Promoção B: desconto de 15%
promocao_b = celular * 0.15
final_b = celular - promocao_b

# Exibe os valores finais das promoções
print(f'O valor final na promoção A (10%): R$ {final_a:.2f}')
print(f'O valor final na promoção B (15%): R$ {final_b:.2f}')

# Mensagem explicando qual promoção é melhor
print('A promoção B vale mais a pena, pois o desconto é maior!')
