#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(0,10)
print('Olá, Sou seu Computador\nAcabei de pensar em um numero entre 0 e 10\nSerá que voce consegue advinhar?')
acertou = False
tentativa = 0
while not acertou:
    jogador = int(input('Digite um palpite '))
    tentativa += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente de novo!')
        elif jogador > computador:
            print('Menos...Tente de novo!')    

print(f'Voce acertou com {tentativa} tentativas')



