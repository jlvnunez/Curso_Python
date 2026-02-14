#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import os
os.system('')
from random import randint
from time import sleep
#          0       1      2
itens = ('pedra', 'papel','tesoura')
# O computador sorteia um índice (0, 1 ou 2)
computador = randint(0,2)
#print(f'O computador escolheu {itens[computador]}')
print("=" *5 + "Game JOKENPÔ" +"=" * 5 )


print(''' Suas Opções
      [0]Pedra 
      [1]Papel
      [2]Tesoura''')
jogador = int(input('Qual a sua Jogada? '))

if jogador > 2 or jogador < 0:
  print('\033[1;31mJOGADA INVALIDA !\033[m')
else:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ!!')
    print('-=' *11)
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador Jogou {itens[jogador]}')
    print('-=' *11)

    if computador == 0: #computador jogou pedra
       if jogador == 0:#pedra
          print('\033[1;34mEMPATE!!\033[m')
       elif jogador == 1:#papel
          print('\033[1;32mJOGADOR GANHOU!\033[m')
       elif jogador == 2:#tesoura
          print('\033[1;31mCOMPUTADOR GANHOU !\033[m')
      
    elif computador == 1: #computador jogou papel
        if jogador == 0:#pedra
          print('\033[1;31mCOMPUTADOR GANHOU !\033[m')
        elif jogador == 1:#papel
           print('\033[1;34mEMPATE!!\033[m')
        elif jogador ==2:#tesoura
           print('\033[1;32mJOGADOR GANHOU!\033[m')
        

    elif computador == 2: #computador jogou tesoura
        if jogador == 0: #pedra
            print('\033[1;32mJOGADOR GANHOU!\033[m')
        elif jogador == 1: #papel
            print('\033[1;31mCOMPUTADOR GANHOU !\033[m')
        elif jogador ==2: #tesoura
            print('\033[1;34mEMPATE!!\033[m')

    

input('tecle enter para encerrar...')   



