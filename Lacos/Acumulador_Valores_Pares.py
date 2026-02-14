# Inicializa o contador de números pares
cont = 0

# Inicializa a variável que armazenará a soma dos números pares
soma = 0

# Laço que se repete 6 vezes (de 1 até 6)
for c in range(1, 7): 
    
    # Solicita ao usuário que digite um número
    num = int(input(f'Digite o {c}º número: '))
    
    # Verifica se o número digitado é par
    # Se o resto da divisão por 2 for 0, o número é par
    if num % 2 == 0: 
        
        # Incrementa o contador de números pares
        cont += 1
        
        # Adiciona o número à soma
        soma += num

# Exibe o resultado final
print(f'Você informou {cont} valores pares e a soma deles é {soma}.')
