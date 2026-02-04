# Pede ao usuário a idade do carro e converte a resposta para número inteiro
tempo = int(input('quanto tempo tem seu carro? '))

# Verifica se o tempo do carro é menor ou igual a 3 anos
if tempo <= 3:
    # Se a condição for verdadeira, o carro é considerado novo
    print('seu carro é novo')
else:
    # Caso contrário, o carro é considerado velho
    print('seu carro é velho')
