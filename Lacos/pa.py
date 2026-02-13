# Pede ao usuário o primeiro termo da PA e converte para inteiro
primeiro = int(input('Digite o primeiro termo: '))

# Pede ao usuário a razão (quanto vai somar a cada passo)
razao = int(input('Digite a razão: '))

# A variável "termo" começa com o valor do primeiro termo
termo = primeiro

# Repete 10 vezes (vai mostrar 10 termos da PA)
for c in range(0, 10):

    # Mostra o valor atual do termo
    print(termo)

    # Atualiza o termo somando a razão
    # Isso faz ele crescer a cada repetição
    termo = termo + razao
