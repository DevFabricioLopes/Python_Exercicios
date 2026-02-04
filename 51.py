# pede ao usuário a velocidade atual do carro
# o valor é convertido para float para permitir casas decimais
velocidade = float(input('Qual é a velocidade do carro: '))

# verifica se a velocidade ultrapassa o limite de 80 km/h
if velocidade > 80:
    
    # calcula a multa diretamente:
    # (velocidade - 80) -> quanto passou do limite
    # * 7              -> valor da multa por km excedido
    multa = (velocidade - 80) * 7
    
    # exibe a mensagem informando que o limite foi ultrapassado
    print('Sua velocidade está acima do permitido.')
    
    # exibe o valor da multa calculada
    print(f'Multa: R$ {multa:.2f}')

else:
    # caso a velocidade esteja dentro do limite permitido
    print('Você está dentro do limite permitido.')
