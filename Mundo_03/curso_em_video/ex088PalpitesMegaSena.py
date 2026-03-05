#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print('-='*25)
print('     PALPITES DA MEGA SENA V1.0     ')
print('-='*25)

lista=[]
jogos=[]
qtd = int(input('Quantos jogos voce quer fazer? '))
total=1
while total <= qtd:
    cont=0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >=6:
            break    
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total+=1
print('=' *5,f'Sorteando {qtd} Jogos','='*5)
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)    
print('='*5,'<BOA SORTE!!>','='*5)