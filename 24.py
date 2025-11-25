
peso=float(input('digite seu peso: '))
altura = float(input('digite sua altura '))
imc = peso / ( altura**2)

if imc < 18.5:  
   print(f' vc esta abaixo do peso: ')
elif imc >= 18.5 and imc <= 24.9:
   print(f' vc esta no peso normal: ')
elif   imc >= 25 and imc <= 29.9: 
   print( f' vc esta sobrePeso: ')
else: 
    print(f' vc esta obeso')
