# Lê o nome digitado pelo usuário, transforma todas as letras em maiúsculas
# e remove espaços extras no início e no fim com .strip()
# Isso facilita a contagem e a busca da letra "A", sem se preocupar com maiúsculas/minúsculas ou espaços
nome = input('Digite o nome: ').upper().strip()

# Mostra quantas vezes a letra "A" aparece no nome
# nome.count("A") retorna o número de vezes que "A" aparece na string
print(f'A letra "A" aparece no nome {nome} o número de {nome.count("A")} vezes')

# Mostra a posição da primeira letra "A" no nome
# nome.find("A") retorna o índice da primeira ocorrência da letra "A"
# Adicionamos +1 porque Python começa a contar do 0, mas queremos posição humana
print(f'A primeira letra "A" apareceu na posição {nome.find("A")+1}')

# Mostra a posição da última letra "A" no nome
# nome.rfind("A") retorna o índice da última ocorrência da letra "A"
# Adicionamos +1 para mostrar a posição de forma humana
print(f'A última letra "A" apareceu na posição {nome.rfind("A")+1}')
