# Pede ao usuário o primeiro termo da PA
primeiro_termo = int(input('Digite o primeiro termo: '))

# Pede ao usuário a razão da PA
razao = int(input('Digite a razão: '))

# Calcula o décimo termo usando a fórmula da PA:
# an = a1 + (n - 1) * r
# Aqui n = 10
decimo = primeiro_termo + (10 - 1) * razao

# O laço começa no primeiro termo,
# vai até o décimo termo,
# pulando de acordo com a razão.
# Usamos (decimo + razao) porque o range não inclui o último valor.
for c in range(primeiro_termo, decimo + razao, razao):
    
    # Mostra cada termo da PA na mesma linha
    print(c, end=" -> ")

# Indica o final da sequência
print("FIM")
