# pede ao usuário um número inteiro
num = int(input('Digite um número inteiro: '))

# verifica se o número é par ou ímpar
# num % 2 -> calcula o resto da divisão por 2
# se o resto for 0, o número é par
if num % 2 == 0:
    
    # \033[32m  -> muda a cor do texto para verde
    # \033[m    -> volta a cor padrão do terminal
    print(f'\033[32mO número {num} é PAR\033[m')

else:
    # \033[31m  -> muda a cor do texto para vermelho
    # \033[m    -> volta a cor padrão do terminal
    print(f'\033[31mO número {num} é ÍMPAR\033[m')
