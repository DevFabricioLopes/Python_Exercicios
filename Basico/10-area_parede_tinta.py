# Solicita ao usuário a largura da parede
# O valor é convertido para float para permitir números decimais
larg = float(input('Digite a largura da parede: '))

# Solicita ao usuário a altura da parede
# Também convertido para float
alt = float(input('Digite a altura da parede: '))

# Calcula a área da parede (largura × altura)
area = larg * alt

# Calcula a quantidade de tinta necessária
# Considerando que 1 litro de tinta cobre 3 m²
tinta = area / 3

# Exibe os resultados
print(
    f'A largura da parede é: {larg}, '
    f'a altura da parede é: {alt}, '
    f'a área total da parede é: {area:.2f} m² '
    f'e a quantidade de tinta necessária é: {tinta:.2f} litros'
)
