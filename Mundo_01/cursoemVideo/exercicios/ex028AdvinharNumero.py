 #Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(
    0,5)#faz computador pensar
print('-=-' *15)
print('Vou pensar em um numero entre 0 e 5')
print('-=-' *15)
jogador= int(input('Em que numero eu pensei? '))#jogador tenta advinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabens, Voce acertou!')
else:
    print('Que pena,Voce errou!')
    print(f'Eu pensei no numero {computador} e não no numero {jogador}')
    
