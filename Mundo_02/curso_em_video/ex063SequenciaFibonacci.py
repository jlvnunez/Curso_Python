#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
from time import sleep
print('~' *20)
print('SEQUENCIA FIBONACCI')
print('~' *20)
n = int(input('Quantos termos voce quer mostrar  '))
t1=0
t2=1
print('~' *30)
print(f'\033[1;32m{t1} -> {t2}->\033[m',end='',flush=True)
sleep(0.3) # Pausa antes de começar o loop
cont = 3
while cont <= n:
    t3 = t1+t2
    print(f' \033[1;32m{t3}->\033[m',end='',flush=True)# flush=True força o Python a mostrar na tela na hora
    sleep(0.3)# <--- AQUI! Ele espera 0.3 segundo a cada repetição
    t1=t2
    t2=t3
    cont += 1
print('FIM!')
print(f'Pronto! Foram exibidos os \033[1;31m{n} primeiros termos da sequência.\033[m')
