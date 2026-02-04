# Pede ao usuário a velocidade do carro em km/h
velo = float(input(' qual e a velocidade do carro: '))

# Define o limite máximo de velocidade permitido
limite = 80

# Verifica se a velocidade é maior ou igual ao limite
if velo >= 80: 
    # Mensagem informando que o motorista ultrapassou o limite
    print(f' Vc ultrapassou o limite de velocidade e foi multado: ')
    
    # Calcula quantos km/h acima do limite o carro estava
    excesso = velo - limite
    
    # Calcula o valor da multa (R$7 por km acima do limite)
    multa = excesso * 7
    
    # Mostra o valor total da multa
    print(f' o valor da multa e: {multa}')
    
# Caso a velocidade esteja dentro do permitido
else: 
    print(f' parabens vc andou dentro do permitido!')   
