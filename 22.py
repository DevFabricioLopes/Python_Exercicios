valor=int(input('digite o valor da compra: '))
km = float(input('digite a distancia em km:  '))
if valor >= 300: 
    print(' o frete e gratis. ')
elif valor < 300 and km <= 50: 
    print(' o frete custa 20 reais: ')
else:
    print(' o  valor do frete e 35 reais: ')

print( f' o valor da compra e: {valor} ')



