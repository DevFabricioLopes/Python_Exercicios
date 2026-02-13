# Conta quantas letras existem em um texto
# Comentário explicando o objetivo do programa

# Solicita que o usuário digite um texto
# input() sempre retorna uma string
texto = input('Digite um texto: ')

# Cria uma variável chamada contador e inicia com 0
# Ela será usada para contar a quantidade de caracteres
contador = 0

# Loop que percorre cada caractere da string digitada
# A cada repetição, 'letra' recebe um caractere do texto
for letra in texto:

    # Incrementa o contador em 1 a cada caractere percorrido
    # contador += 1 é o mesmo que: contador = contador + 1
    contador += 1

# Exibe o total de caracteres contados
# f-string permite inserir a variável dentro da string usando { }
print(f'O texto possui {contador} letras')
