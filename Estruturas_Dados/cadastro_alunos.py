# Lista que vai armazenar todos os alunos
alunos = []

# Pergunta quantos alunos serão cadastrados
qtd = int(input('Quantos alunos deseja cadastrar? '))

# Loop para cadastrar cada aluno
for i in range(qtd):
    
    # Dicionário para guardar os dados de UM aluno
    aluno = {}
    
    # Entrada do nome do aluno
    aluno['nome'] = input('Digite o nome do aluno: ')
    
    # Entrada da nota do aluno
    aluno['nota'] = float(input('Digite a nota do aluno: '))
    
    # Adiciona o dicionário aluno dentro da lista alunos
    alunos.append(aluno)

print('-' * 40)
print('LISTA DE ALUNOS')
print('-' * 40)

# Variável para somar todas as notas
soma = 0

# Percorre a lista de alunos
for aluno in alunos:
    print(f"Aluno: {aluno['nome']} | Nota: {aluno['nota']}")
    soma += aluno['nota']

# Calcula a média da turma
media = soma / qtd

print('-' * 40)
print(f'Média da turma: {media:.2f}')
print('-' * 40)

# Mostra alunos aprovados e reprovados
for aluno in alunos:
    if aluno['nota'] >= 7:
        print(f"{aluno['nome']} está APROVADO")
    else:
        print(f"{aluno['nome']} está REPROVADO")
