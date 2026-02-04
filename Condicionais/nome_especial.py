# Pede ao usuário que digite o nome
nome = str(input('qual seu nome: ')).strip()

# Verifica se o nome digitado é exatamente "Gustavo"
if nome == 'Gustavo':
    # Se for Gustavo, mostra uma mensagem especial
    print('Que nome lindo você tem!')

# Esta mensagem será exibida para qualquer nome
print(f'Bom dia, {nome}')
