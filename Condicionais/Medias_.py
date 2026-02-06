# Solicita ao usuário a primeira nota
# O input() retorna texto, então usamos int() para converter para número inteiro
n1 = float(input('Qual é a sua primeira nota: '))

# Solicita ao usuário a segunda nota
n2 = float(input('Qual é a sua segunda nota: '))

# Calcula a média das duas notas
media = (n1 + n2) / 2

# Verifica se a média é menor que 5
if media < 5:
    # Média abaixo de 5 → aluno reprovado
    print(f'Sua média é {media}, você está reprovado!')

# Verifica se a média está entre 5 e 6.9
elif media >= 5 and media < 6.9:
    # Média entre 5 e 6.9 → aluno em recuperação
    print(f'Sua média é {media}, você está em recuperação!')

# Caso a média seja 7 ou maior
else:
    # Média maior ou igual a 7 → aluno aprovado
    print(f'Sua média é {media}, você está aprovado!')
