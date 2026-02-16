#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
print('=' *20)
print('Numeros Primos')
print('=' *20)
num =int(input('Digite um numero '))
total = 0
for c in range(1,num +1):
    if num % c == 0:
        print('\033[33m', end=' ') # Amarelo para divisores
        total+= 1
    else:
        print('\033[31m', end=' ') # Vermelho para os demais
    print(f'{c}', end='')    
print(f'\n\033[mO numero {num} foi dividido {total} vezes')
if total ==2:
    print(f'Portanto,o numero {num} é PRIMO')
else:
    print(f'Portanto,o {num} Nao é PRIMO')
