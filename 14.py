produto = float(input('digite o valor do produto: R$'))
desconto = produto*0.05
preco_final= produto - desconto 
print(f' o produto custava R${produto}, na promoção com desconto de 5% vai custar R${preco_final:.2f}')

