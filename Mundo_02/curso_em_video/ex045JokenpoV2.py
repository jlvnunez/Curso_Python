#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import os
os.system('')
from random import randint
from time import sleep

def limpar():
    # 'cls' para Windows, 'clear' para Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')
#          0       1      2
itens = ('pedra', 'papel','tesoura')
# Variáveis do Placar (começam em zero fora do loop)
vitorias_jogador = 0
vitorias_computador = 0

while True:
    limpar() # <-- CHAMADA DA FUNÇÃO AQUI para começar cada rodada com a tela limpa
    
    # O computador sorteia um índice (0, 1 ou 2)
    computador = randint(0,2)
    print("=" *5 + "Game JOKENPÔ" +"=" * 5 )
    print(f'''
    PLACAR: JOGADOR {vitorias_jogador} x {vitorias_computador} COMPUTADOR
    -----------------------
    Suas Opções:
    [0] Pedra 
    [1] Papel
    [2] Tesoura''')
    try:
      jogador = int(input('Qual a sua Jogada? '))
    except ValueError:
       print('\033[1;31mERRO: Digite apenas números entre 0 e 2!\033[m')
       sleep(2)
       continue # Volta para o início do loop
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
              vitorias_jogador +=1
           elif jogador == 2:#tesoura
              print('\033[1;31mCOMPUTADOR GANHOU !\033[m')
              vitorias_computador +=1
      
        elif computador == 1: #computador jogou papel
            if jogador == 0:#pedra
              print('\033[1;31mCOMPUTADOR GANHOU !\033[m')
              vitorias_computador += 1
            elif jogador == 1:#papel
               print('\033[1;34mEMPATE!!\033[m')
            elif jogador ==2:#tesoura
               print('\033[1;32mJOGADOR GANHOU!\033[m')
               vitorias_jogador +=1
        

        elif computador == 2: #computador jogou tesoura
            if jogador == 0: #pedra
                print('\033[1;32mJOGADOR GANHOU!\033[m')
                vitorias_jogador += 1
            elif jogador == 1: #papel
                print('\033[1;31mCOMPUTADOR GANHOU !\033[m')
                vitorias_computador += 1
            elif jogador ==2: #tesoura
                print('\033[1;34mEMPATE!!\033[m')

     # A identação aqui é a chave: fora dos IFs de resultado, mas dentro do WHILE
    print('-=' * 11)
    continuar = input('Quer jogar de novo? [S/N] ').strip().upper()
    if continuar == 'N':
      break


print('Até a próxima!')           

    

input('tecle enter para encerrar...')   



