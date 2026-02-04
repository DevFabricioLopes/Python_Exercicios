# Mostra a tabuada de um número digitado

numero = int(input('Digite um número: '))

for contador in range(1, 11):
    resultado = numero * contador
    print(f'{numero} x {contador} = {resultado}')
