# Programa que sorteia uma música aleatoriamente
# usando a biblioteca random

# Importa o módulo random para sorteios
import random

# Solicita os nomes das músicas
m1 = input('Digite o nome da primeira música: ')
m2 = input('Digite o nome da segunda música: ')
m3 = input('Digite o nome da terceira música: ')
m4 = input('Digite o nome da quarta música: ')

# Cria uma lista com as músicas informadas
lista_musicas = [m1, m2, m3, m4]

# Sorteia uma música aleatoriamente da lista
sorteio = random.choice(lista_musicas)

# Exibe o resultado do sorteio
print(f'A música escolhida foi: {sorteio}')
