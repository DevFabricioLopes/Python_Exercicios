# Solicita ao usuário o ano de nascimento
# Converte a entrada (texto) para número inteiro
ano_nascimento = int(input('Qual ano você nasceu? '))

# Calcula a idade da pessoa com base no ano atual (2026)
idade = 2026 - ano_nascimento

# Verifica se a idade é de até 9 anos
if idade <= 9:
    # Categoria Mirim
    print('Você é atleta Mirim')

# Verifica se a idade está entre 10 e 14 anos
elif idade >= 10 and idade <= 14:
    # Categoria Infantil
    print('Você é atleta Infantil')

# Verifica se a idade está entre 15 e 19 anos
elif idade >= 15 and idade <= 19:
    # Categoria Júnior
    print('Você é atleta Júnior')

# Verifica se a idade é exatamente 20 anos
elif idade == 20:
    # Categoria Sênior
    print('Você é atleta Sênior')

# Caso a idade seja maior que 20 anos
else:
    # Categoria Master
    print('Você é atleta Master')
