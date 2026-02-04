# Programa que lê um número de 0 a 9999 e mostra cada dígito separado

num = int(input("Digite um número de 0 a 9999: "))

unidade = num % 10
dezena = (num // 10) % 10
centena = (num // 100) % 10
milhar = (num // 1000) % 10

print(f"Milhar: {milhar}")
print(f"Centena: {centena}")
print(f"Dezena: {dezena}")
print(f"Unidade: {unidade}")
