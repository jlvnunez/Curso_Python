#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
totalMaior=0
totalMenor=0
for pessoa in range(1,8):
   nasc = int(input(f'Nascimento da {pessoa}° pessoa '))
   idade = atual - nasc
   print(f'Essa pessoa tem {idade} anos.')
   if idade > 21: 
     totalMaior += 1
   else:
    totalMenor += 1
print(f'Total de pessoas Maiores de idade: {totalMaior}')
print(f'Total de pessoas menores de idade: {totalMenor} ')


