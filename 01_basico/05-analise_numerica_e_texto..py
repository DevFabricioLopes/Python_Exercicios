# ==============================
# PARTE 1 — ANÁLISE NUMÉRICA
# ==============================

# Solicita um número inteiro ao usuário
num = int(input('Digite um número: '))

# Exibe o tipo primitivo do valor informado
print(f'O tipo primitivo é: {type(num)}')

# Operações matemáticas básicas
print(f'Dobro: {num * 2}')
print(f'Triplo: {num * 3}')
print(f'Raiz quadrada: {num ** 0.5}')

# Verificações lógicas
print(f'É par? {num % 2 == 0}')
print(f'É ímpar? {num % 2 != 0}')
print(f'É positivo? {num > 0}')
print(f'É negativo? {num < 0}')

# Antecessor e sucessor
print(f'Antecessor: {num - 1}')
print(f'Sucessor: {num + 1}')


# ==============================
# PARTE 2 — ANÁLISE DE TEXTO
# ==============================

# Solicita uma entrada de texto ao usuário
texto = input('Digite algo: ')

# Exibe o tipo primitivo do texto
print(f'O tipo primitivo é: {type(texto)}')

# Verificações usando métodos de string
print(f'É numérico? {texto.isnumeric()}')
print(f'É alfabético? {texto.isalpha()}')
print(f'É alfanumérico? {texto.isalnum()}')
print(f'Tudo maiúsculo? {texto.isupper()}')
print(f'Tudo minúsculo? {texto.islower()}')
print(f'Está capitalizada? {texto.istitle()}')

# Conta o total de caracteres digitados
print(f'Total de caracteres: {len(texto)}')
