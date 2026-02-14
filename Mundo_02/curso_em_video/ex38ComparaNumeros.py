#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

n1 = int(input('Digite o primeiro numero '))
n2 = int(input('Digite o segundo numero '))

if n1 > n2:
    print('\033[32mO primeiro valor é MAIOR!\033[m')
elif n1 == n2:
    print(f'\033[32mOs dois valores são iguais!\033[m')
else:
    n2 > n1
    print('\033[32mO segundo valor é MAIOR!\033[m')


input('\033[31mclique enter para fechar....\033[m')    
