#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
verde ='\033[32m'
vermelho = '\033[31m'
reset = '\033[m'

n = int(input('Digite um numero inteiro '))
if n % 2 == 0:
    print(f'{verde} numero digitado é PAR{reset}')
else:
    print(f'{vermelho}O numero digitado é IMPAR{reset}')