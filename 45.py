# Pede ao usuário a distância da viagem em quilômetros
# input() recebe o valor como texto, por isso usamos float() para permitir números com decimal
km = float(input('Qual é a distância da viagem (km): '))

# Verifica se a distância é menor ou igual a 200 km
if km <= 200:
    # Se for até 200 km, o preço da passagem é R$ 0,50 por km
    passagem = km * 0.50
    
    # Exibe o valor da passagem com duas casas decimais
    print(f'O valor da passagem é R$ {passagem:.2f} (até 200 km)')
else:
    # Se a distância for maior que 200 km, o preço da passagem é R$ 0,45 por km
    passagem = km * 0.45
    
    # Exibe o valor da passagem com duas casas decimais
    print(f'O valor da passagem é R$ {passagem:.2f} (acima de 200 km)')
