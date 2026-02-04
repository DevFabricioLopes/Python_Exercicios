# Pede ao usuário que digite a cidade onde nasceu
# strip() remove espaços extras no início ou no final da string
cid = str(input('Em que cidade você nasceu? ')).strip()

# Verifica se os primeiros 5 caracteres da cidade ([:5]) são 'SANTO'
# upper() transforma tudo em maiúsculas para que a comparação seja case-insensitive
# A expressão retorna True se começar com 'SANTO', False caso contrário
print(cid[:5].upper() == 'SANTO')
