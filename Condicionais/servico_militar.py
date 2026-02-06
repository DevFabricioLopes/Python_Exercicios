# Solicita ao usuário o ano de nascimento
# O input() retorna um texto, então usamos int() para converter para número inteiro
ano = int(input('Digite o ano do seu nascimento: '))

# Calcula a idade da pessoa
# 2026 é o ano atual usado como referência
calculo = 2026 - ano

# Verifica se a idade é menor que 18 anos
if calculo < 18:
    # Calcula quantos anos ainda faltam para completar 18 anos
    falta = 18 - calculo
    
    # Exibe a mensagem informando que ainda falta tempo para o alistamento
    print(f'Voce ainda nao se alistou e faltam {falta} anos para vc se alistar')

# Verifica se a idade é exatamente 18 anos
elif calculo == 18:
    # Se a idade for exatamente 18, está no ano correto para o alistamento
    print('Esta na hora de se alistar')

# Caso a idade seja maior que 18 anos
else:
    # Calcula quantos anos já se passaram desde o alistamento (18 anos)
    falta = calculo - 18
    
    # Exibe a mensagem informando que o prazo de alistamento já passou
    print(f'Voce ja passou do tempo de alistamento, pois se passaram {falta} anos do alistamento')
