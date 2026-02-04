# Programa que lê um número de 0 a 9999 e mostra cada dígito separado

# Programa que separa os dígitos de um número inteiro
# considerando milhar, centena, dezena e unidade

# Solicita um número inteiro entre 0 e 9999
num = int(input("Digite um número de 0 a 9999: "))

# Calcula cada dígito usando divisão inteira e resto
unidade = num % 10                  # Último dígito
dezena = (num // 10) % 10           # Segundo dígito
centena = (num // 100) % 10         # Terceiro dígito
milhar = (num // 1000) % 10         # Quarto dígito

# Exibe os resultados
print(f"Milhar: {milhar}")
print(f"Centena: {centena}")
print(f"Dezena: {dezena}")
print(f"Unidade: {unidade}")
