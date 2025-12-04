# # faça um programa em python que abra e reproduza um arquivo de audio mp3 

# import winsound

# # Toca o som de notificação padrão do Windows

# winsound.PlaySound("SystemExit", winsound.SND_ALIAS)






idade = int (input('digite sua idade: '))
if idade >= 18: 
   print(f' vc e maiuor de idade: ')
elif idade >= 12 and idade <= 17: 
   print(f' vc e adolecente')
else: 
   print( f' vc e crianca ')

