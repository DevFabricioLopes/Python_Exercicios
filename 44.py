# Importa o módulo random, que permite gerar números aleatórios
import random

# O computador escolhe um número aleatório entre 0 e 5
pc = random.randint(0, 5)

# Pede para o usuário digitar o número que ele acha que o computador pensou
# int() transforma o que foi digitado em número
user = int(input('Qual foi o número que o PC pensou? '))

# Verifica se o número do usuário é igual ao número do computador
if pc == user: 
    # Executa este print se o usuário acertar
    print('Você venceu!')
else: 
    # Executa este print se o usuário errar
    # Mostra também qual era o número correto
    print(f'Você perdeu! O número era {pc}')
