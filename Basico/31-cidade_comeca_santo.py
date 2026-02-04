# Programa que verifica se a cidade onde a pessoa nasceu
# começa com o nome "SANTO"

# Pede ao usuário o nome da cidade
# strip() remove espaços extras no início e no fim da string
cidade = input('Em que cidade você nasceu? ').strip()

# Verifica se os primeiros 5 caracteres da cidade são "SANTO"
# upper() garante que a comparação não dependa de maiúsculas/minúsculas
comeca_santo = cidade[:5].upper() == 'SANTO'

# Exibe o resultado (True ou False)
print(comeca_santo)
