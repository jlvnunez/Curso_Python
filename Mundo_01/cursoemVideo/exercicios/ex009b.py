#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Digite um número para ver sua tabuada: '))

print(f'\n--- Tabuada do {n} (usando laço for com funcao range) ---')

# O range(1, 11) vai de 1 até 10
for i in range(1, 11):
    resultado = n * i
    print(f'{n} x {i:2} = {resultado}') #o {i:2} para alinhar os numeros

print('-' * 15)