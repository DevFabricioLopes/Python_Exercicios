# Importa a classe date para trabalhar com datas
from datetime import date

# Pede ao usuário o ano de nascimento e converte para inteiro
ano_nascimento = int(input('Qual ano você nasceu? '))

# Obtém o ano atual automaticamente pelo sistema
ano_atual = date.today().year

# Calcula a idade subtraindo o ano de nascimento do ano atual
idade = ano_atual - ano_nascimento

# Se a idade for menor ou igual a 9 anos
if idade <= 9:
    # Categoria Mirim
    print('Você é atleta Mirim')

# Se a idade for até 14 anos (e maior que 9)
elif idade <= 14:
    # Categoria Infantil
    print('Você é atleta Infantil')

# Se a idade for até 19 anos (e maior que 14)
elif idade <= 19:
    # Categoria Júnior
    print('Você é atleta Júnior')

# Se a idade for até 25 anos (e maior que 19)
elif idade <= 25:
    # Categoria Sênior
    print('Você é atleta Sênior')

# Se a idade for maior que 25 anos
else:
    # Categoria Master
    print('Você é atleta Master')
