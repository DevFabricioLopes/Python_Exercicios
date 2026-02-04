# Calcula a área de uma parede e a quantidade de tinta necessária

largura = int(input('Digite a largura da parede: '))
altura = int(input('Digite a altura da parede: '))

# Cálculo da área
area = largura * altura

# Cada litro de tinta cobre 3 m²
tinta = area / 3

print(f'A área da parede é {area} m²')
print(f'Você precisará de {tinta:.2f} litros de tinta')
