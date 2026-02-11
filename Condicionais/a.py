from random import randint

print(' =-= ' * 10)
print(f' JokenPô" ')
print(' =-= ' * 10)

print(f' Escolha Suas Opções: ')

print(f' [1] Pedra ')
print(f' [2] Papel ')
print(f' [3] Tesoura ')

user = int(input(f' Escolha a Opcao : 1 2 ou 3: '))
print(f' o usuario escolheu {user}')

pc = randint(1,3) 
print(f' o pc escolheu {pc}')



if user == pc: 
    print(f' deu empate! ')

elif user == 1 and pc == 2: 
    print(f' pc ganhou : ')    


elif user == 2 and pc == 3:
    print(f' pc ganhou')        

elif user == 3 and pc == 2:
    print(f' usuario ganhou: ')    

elif  user == 1 and pc == 3: 
    print(f' pc ganhou')    

elif user == 3 and pc == 1: 
    print(f' user ganhou')    



else: 
    print(f' Opcao Invalida:')










