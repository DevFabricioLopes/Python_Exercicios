# Pede um número ao usuário e converte para inteiro
num = int(input(' Digite um numero: '))

# Variável que vai contar quantos divisores o número possui
cont = 0

# Laço que percorre todos os números de 1 até o número digitado
for c in range(1, num+1 ): 

    # Verifica se o número digitado é divisível por c
    if num % c == 0: 
        
        # Se for divisível, soma 1 ao contador
        cont += 1   

        # Ativa a cor amarela no terminal (para divisores)
        print(f' \033[33m', end = '')
    
    else:
        # Se não for divisível, ativa a cor vermelha
        print(f' \033[31m', end = '')

    # Imprime o valor atual de c na mesma linha
    print(c, end ='')

# Quebra a linha, reseta a cor e mostra quantas vezes o número foi divisível
print(f' \n\033[m  o numero {num} foi divisivel {cont} vz')

# Verifica se o número tem exatamente 2 divisores
if cont == 2:
    # Se tiver 2 divisores (1 e ele mesmo), é primo
    print(f' E um numero primo! ')
else:
    # Caso contrário, não é primo
    print(f' Nao e um numero primo! ')
