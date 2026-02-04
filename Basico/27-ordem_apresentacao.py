# Programa que sorteia a ordem de apresentação dos alunos
# utilizando a função shuffle da biblioteca random

# Importa apenas a função shuffle
from random import shuffle

# Entrada dos nomes dos alunos
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

# Cria uma lista com os nomes informados
lista_alunos = [n1, n2, n3, n4]

# Embaralha a lista alterando a ordem dos elementos
shuffle(lista_alunos)

# Exibe a ordem sorteada
print('A ordem de apresentação será:')
print(lista_alunos)
