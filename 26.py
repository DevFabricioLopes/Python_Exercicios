dias= int(input(f' quantos dias alugados? '))
km =  float(input('quantos km rodados? '))
dia_alugado = 60
km_rodado = 0.15
total_dias = (dias * dia_alugado) + (km * km_rodado )


print(f' o total a pagar e: {total_dias}')

