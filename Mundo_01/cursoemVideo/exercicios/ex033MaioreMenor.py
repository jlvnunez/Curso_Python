#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('='*30)
a = int(input('Digite o primeiro valor '))
b = int(input('Digite o segundo valor '))
c = int(input('Digite o terceiro valor '))

menor = a
if b<a and b<c:
    menor = b

if c<a and c<b:
    menor = c

maior = a 
if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

print('='*30)
print(f'O maior valor digitado é: {maior}')
print(f'O menor valor digitado é: {menor}')


