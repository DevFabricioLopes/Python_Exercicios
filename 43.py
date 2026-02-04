# Pede ao usuário o consumo do mês e converte para número decimal
consumo = float(input(' Qual foi o consumo do mes:? '))

# Define o consumo ideal (limite)
limite = 30 

# Verifica se o consumo foi MENOR que o limite
if consumo < 30: 
    # Calcula quanto foi economizado (limite menos o consumo)
    economia = limite - consumo
    
    # Cada unidade economizada vale 1 ponto de crédito
    credito = economia 
    
    # Mostra a economia e os pontos ganhos
    print(f' vc economizou {economia} e ganhou {credito} pontos')

# Verifica se o consumo foi MAIOR que o limite
elif consumo > 30: 
    # Calcula o excesso de consumo
    excesso = consumo - limite
    
    # Cada unidade excedente gera 3 pontos de multa
    multa = excesso * 3
    
    # Mostra o excesso e o valor da multa
    print(f'o excesso ficou em {excesso} e a multa ficou em {multa} reais ')

# Caso o consumo seja EXATAMENTE igual ao limite
else:
    # Informa que o consumo foi adequado
    print(f' o consumo foi adequado')    
