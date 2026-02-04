# Conta quantas letras existem em um texto

texto = input('Digite um texto: ')
contador = 0

for letra in texto:
    contador += 1

print(f'O texto possui {contador} letras')
