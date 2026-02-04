# Programa que lê números inteiros até o usuário digitar 0
# e exibe estatísticas sobre os valores informados

# Inicialização das variáveis
quantidade = 0
soma = 0
maior = None
menor = None

while True:
    # Solicita um número ao usuário
    numero = int(input('Digite um número (0 para sair): '))

    # Condição de parada
    if numero == 0:
        break

    # Atualiza quantidade e soma
    quantidade += 1
    soma += numero

    # Verifica maior e menor número
    if maior is None or numero > maior:
        maior = numero

    if menor is None or numero < menor:
        menor = numero

# Evita divisão por zero caso nenhum número seja digitado
if quantidade > 0:
    media = soma / quantidade
else:
    media = 0

# Exibe os resultados finais
print('\n📊 Estatísticas dos números digitados:')
print(f'Quantidade de números: {quantidade}')
print(f'Soma dos números: {soma}')
print(f'Média dos números: {media:.2f}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
