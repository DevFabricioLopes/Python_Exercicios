velo= float(input(' qual e a velocidade do carro: '))
limite = 80
if velo >= 80: 
 
    print(f' Vc ultrapassou o limite de velocidade e foi multado: ')
    excesso = velo - limite
    multa = excesso * 7
    print(f' o valor da multa e: {multa}')

    
else: 
    print(f' parabens vc andou dentro do permitido!')   

