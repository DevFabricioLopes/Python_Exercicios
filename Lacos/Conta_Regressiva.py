# Importa a função sleep do módulo time
# sleep() serve para pausar a execução do programa por um tempo em segundos
from time import sleep  

# Loop que faz uma contagem regressiva de 10 até 1
# range(início, fim, passo)
# Começa em 10, vai até 1 (0 não incluso), decrementando de 1 em 1
for c in range(10, 0, -1):

    # Imprime o número atual da contagem
    print(c)

    # Pausa o programa por 1 segundo antes de continuar para o próximo número
    sleep(1)

# Após terminar o loop (quando chega ao 1),
# imprime a mensagem final com emojis de explosão e festa
print(f'💥🎉🎆  Feliz Ano Novo! ')
