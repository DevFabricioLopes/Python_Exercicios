# Programa que calcula o preço final de um produto com desconto

# Solicita ao usuário o valor original do produto
# Usamos float para permitir valores com centavos
produto = float(input('Digite o valor do produto: R$ '))

# Calcula o valor do desconto (5% do preço do produto)
desconto = produto * 0.05

# Calcula o preço final subtraindo o desconto
preco_final = produto - desconto

# Exibe o resultado formatado com duas casas decimais
print(f'O produto custava R$ {produto:.2f}, '
      f'na promoção com desconto de 5% vai custar R$ {preco_final:.2f}')
