# Solicita ao usuário um valor em metros
# O input retorna uma string, por isso usamos float() para converter para número decimal
metros = float(input('Digite quantos metros: '))

# Converte metros para centímetros
# 1 metro equivale a 100 centímetros
centimetros = metros * 100

# Converte metros para milímetros
# 1 metro equivale a 1000 milímetros
milimetros = metros * 1000

# Exibe os valores convertidos usando f-string
# f-string permite inserir variáveis diretamente dentro do texto
print(
    f'Os metros são: {metros}, '
    f'os centímetros são: {centimetros} '
    f'e os milímetros são: {milimetros}'
)
