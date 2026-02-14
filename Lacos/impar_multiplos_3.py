# Inicializa a variável soma com valor 0.
# Ela armazenará a soma dos valores que atendem à condição.
soma = 0 

# Inicializa o contador.
# Ele contará quantos valores atenderam à condição.
cont = 0

# O laço for percorre os números de 0 até 500 (inclusive),
# pulando de 2 em 2, ou seja, apenas números pares.
for c in range(0, 501, 2):
    
    # Verifica se o número atual (c) é divisível por 3.
    # Se o resto da divisão por 3 for 0, ele é múltiplo de 3.
    if c % 3 == 0: 
        
        # Incrementa o contador
        cont += 1
        
        # Soma o valor de c à variável soma
        soma += c

# Exibe o resultado final
print(f'A soma de todos os {cont} valores solicitados é: {soma}')
