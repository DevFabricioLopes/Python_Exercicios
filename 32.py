#professor que sortear a ordem de apresentação dos alunos. faça um programa que leia o nome dos quatros e  mostre a ordem sorteada..
from random import shuffle
n1= (input('digite o seu nome: '))
n2= (input('digite seu nome: ')) 
n3= (input('digite seu nome: '))
n4= (input('digite seu nome: '))
lista = [n1, n2, n3, n4]  
shuffle(lista)

print(f' a ordem de apresentação sera: ')
print(lista)



