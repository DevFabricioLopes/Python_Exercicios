n= int(input(f' Digite um numero inteiro: '))

print(f' Escolha uma das bases para conversao: ')
print(f'[1] Conveter para Binario: ')
print(f'[2] Converter para Octal  ')
print(f'[3] Converter para Hexadecimal ')

opcao = int(input(f' SUa opcao: '))

if opcao == 1: 
    print(f' o numero escolhido foi: {n} e Convertido em Binario: {bin(n)[2:]}')

elif opcao ==2: 
    print(f' o numero escolhido e: {n} e convertido em octal: {oct(n)[2:]}' )

elif opcao == 3: 
    print(f' o numero escolhido foi: {n} e convertido em Hexadecimal: {hex(n)[2:]}')    

else: 
    print(f' Opção Invalida: ')
          


