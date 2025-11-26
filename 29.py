import math
oposto = float(input('digite o cateto oposto: '))
adjacente = float(input(' digite o cateto adjacente:  '))
hipotenusa = (oposto**2 + adjacente**2)
raiz= math.sqrt(hipotenusa)

print(f' a hipotenusa vai medir: : {raiz:.2f}')


