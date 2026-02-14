# Pede uma frase ao usuário
# strip() remove espaços do começo e do fim
# upper() transforma tudo em maiúsculo
frase = str(input('digite uma frase: ')).strip().upper()

# Divide a frase em palavras usando os espaços como separador
palavras = frase.split()

# Junta novamente as palavras, eliminando os espaços entre elas
# Isso é importante para testar palíndromo sem considerar espaços
junto = "".join(palavras) 

# Cria uma variável vazia que vai armazenar a frase invertida
inverso = ""

# Percorre a string de trás para frente
# len(junto) - 1 → começa na última posição
# -1 → vai até antes do índice -1
# -1 → anda voltando de 1 em 1
for letras in range(len(junto) - 1, -1, -1): 
    
    # Aqui pegamos cada letra pelo índice
    # Usamos colchetes [] para acessar posição da string
    inverso += junto[letras]

# Compara a frase normal com a invertida
if inverso == junto:
    print(f'Temos Palindromo')    
else: 
    print(f'Nao e palindromo')
