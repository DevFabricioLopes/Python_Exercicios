from random import randint
from time import sleep

# Mostra o título do jogo
print('=' * 30)
print('        JOKENPÔ        ')
print('=' * 30)

# Mostra as opções do jogo
print('Escolha uma opção:')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')

# Jogador escolhe uma opção
user = int(input('Sua vez de jogar: '))

# Computador escolhe aleatoriamente
pc = randint(1, 3)

# Pausa para dar efeito visual
sleep(1)
print('\nJO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ!!!\n')
sleep(1)

# Mostra as escolhas
print(f'Você escolheu: {user}')
print(f'Computador escolheu: {pc}')
print('-' * 30)

# Verifica o resultado do jogo

# Caso de empate
if user == pc:
    print('Resultado: EMPATE 🤝')

# Casos em que o jogador ganha
elif (user == 1 and pc == 3) or \
     (user == 2 and pc == 1) or \
     (user == 3 and pc == 2):
    print('Resultado: VOCÊ GANHOU 🎉')

# Caso o jogador perca
elif user in [1, 2, 3]:
    print('Resultado: VOCÊ PERDEU 😢')

# Caso o usuário digite uma opção inválida
else:
    print('Opção inválida! Escolha 1, 2 ou 3.')
