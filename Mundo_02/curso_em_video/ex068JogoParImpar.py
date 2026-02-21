#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
print('Jogo Par ou Impar'.center(50,'='))

from random import randint
v=0
while True:
    jogador = int(input('Digite um valor '))
    computador= randint(0,20)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo =str(input('PAR ou IMPAR? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador} Um total de {total} → ',end='')
    print('\033[1;32mDeu PAR\033[m' if total %2 == 0 else '\033[1;31mDeu Impar\033[m')
    if tipo == 'P':
        if total %2==0:
            print('\033[1;32mVoce Venceu!!!\033[m')
            v+=1
        else:
            print('\033[1;31mVoce Perdeu!!!\033[m')
            break
    elif total %2==1:  
        print('\033[1;32mVoce Venceu!!!\033[m')  
        v+=1
    else:
        print('\033[1;31mVoce Perdeu!!!\033[m')
        break
    print('Vamos Jogar Novamente?')
print(f'Game Over!!- Voce Venceu {v} Vezes')


    
