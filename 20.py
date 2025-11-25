
salario= float(input('digite o valor do  salario: '))
if salario <= 3000: 
   aumento_12= salario*0.12
   novo_salario = salario + aumento_12
   print(f' seu aumento foi de {aumento_12} e o seu novo salario e de : {novo_salario}')  
elif  salario > 3000:
     aumento_08 = salario*0.08
     novo_salario08 = salario + aumento_08 
     print(f' o seu aumento foi de {aumento_08} e o seu novo salario e de: {novo_salario08}')



