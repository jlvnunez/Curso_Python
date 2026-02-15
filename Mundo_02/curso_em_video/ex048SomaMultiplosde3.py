#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 ==0:
        cont = cont + 1
        soma = soma + c
        print(f"\033[1;32m{c}\033[m",end=' ')
print(f'\nA Soma dos {cont} Multiplos de 3 é de : {soma}')

input('Clique enter para encerrar...')
    
    
    