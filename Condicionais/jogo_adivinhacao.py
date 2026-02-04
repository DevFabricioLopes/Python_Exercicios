from random import randint  # importa só a função randint

print('=' * 40)
print('🎲 JOGO DA ADIVINHAÇÃO 🎲')
print('=' * 40)

# o computador sorteia um número entre 0 e 5
pc = randint(0, 5)

# pede o palpite do usuário
user = int(input('Tente adivinhar o número sorteado (0 a 5): '))

print('-' * 40)

# verifica se o usuário acertou
if pc == user:
    print(f'✅ O computador sorteou o número {pc}')
    print('🎉 PARABÉNS! Você acertou!')
else:
    print(f'❌ O computador sorteou o número {pc}')
    print('😢 Que pena! Você errou.')

print('=' * 40)
