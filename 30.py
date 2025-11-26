import math
num=int(input('digite um numero para que possa calcular o angulo do seno, consseno e a tangente: '))
num = math.radians(num)
seno = math.sin(num)
cosseno = math.cos(num)
tangente = math.tan(num)
print(f'Ângulo em radianos: {num:.2f}')
print(f' o valor do seno é {seno:.2f}')
print(f' o valor do cosseno e: {cosseno:.2f}')
print(f' o valor da tangente e: {tangente:.2f}')



