valor_imovel = float(input('Qual é o valor do imóvel? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos pretende pagar o financiamento? '))

if anos <= 20: 
    valor_final = valor_imovel * 0.05

elif anos > 21 and anos <= 30: 
    valor_final = valor_imovel 
    
elif anos > 30: 
    valor_final = valor_imovel * 1.10

else: 
    print(f'')

prestacao = valor_final / (anos * 12)
limite = salario * 0.30

print(f' Valor final do imovel: R${valor_final}')
print(f' o valor da prestacao: R${prestacao}')


if prestacao > limite: 
   print(f' Emprestimo Negado!')


else:
    print(f' Emprestimo aprovado! ') 


      
