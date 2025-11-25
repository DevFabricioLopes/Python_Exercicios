produto= float(input('digite o valor do produto> '))
desconto= produto*0.05
avista= produto - desconto 
dinheiro = produto*0.08
desconto_dinheiro = produto - dinheiro
print(f' seu desconto no pagamento avista ficou em> {avista}')
print(f' seu desconto no pagamento com dinheiro ficou em: {desconto_dinheiro}')
