

luz=int(input('digite o valor da conta de luz: ' ))
if luz > 250:
   desconto_5 = luz *0.05
   novaluz_5 = luz - desconto_5
   print(f' o valor do desconto da conta de luz foi de 5% e ficou no valor de {novaluz_5}')
elif  luz >= 150 and luz <= 250:
   desconto_3 = luz*0.03
   novaluz_3 = luz - desconto_3
   print(f' o valor desconto da sua luz foi de 3% e ficou no valor de {novaluz_3}')
else:
   print(f' sua conta nao tem desconto: ')

   print(f' o valor da sua luz foi de: {luz}')


