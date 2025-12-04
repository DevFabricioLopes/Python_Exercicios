#faça um programa  que leia  um numero de 0 a 9999 e mostre na tela cada um dos digitos separados: unidade,dezena, centena e milhar.


n = input("Digite um número de 0 a 9999: ").strip()

# Garante que sempre terá 4 dígitos (ex.: 23 → 0023)
n = n.zfill(4)

print(f"Unidade: {n[3]}")
print(f"Dezena: {n[2]}")
print(f"Centena: {n[1]}")
print(f"Milhar: {n[0]}")

