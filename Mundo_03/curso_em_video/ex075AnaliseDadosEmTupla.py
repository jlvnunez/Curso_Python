#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
'''
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
print()
print(f'{"Analise de dados em Tupla":=^50}')
print('='*50)
num = (int(input('digite o primeiro valor '))),(int(input('digite o segundo valor '))),(int(input('digite o terceiro valor '))),(int(input('digite o quarto valor ')))
print('='*50)
print(f'Voce digitou: {num}')
print(f'O valor 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posicao')
else:
    print('\033[1;31mO valor 3 nao foi digitado em nenhuma posição!\033[m')
print(f'Os valores pares digitados foram: ',end='  ')
for p in num:
    if p %2==0:
        print(p,end=' ')
print(f'\n{'Programa Encerrado':=^50}')


