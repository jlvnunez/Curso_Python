#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
n= int(input('Digite um Numero para calcular seu fatorial  '))
c = n
f = 1
print(f'Calculando \033[1;31m{n}! =\033[m ',end='')
while c > 0:
    print(f'{c}',end ='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print(f'\033[1;32m{f}\033[m')





