'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = int(input('Primeiro Valor '))
n2 = int(input('Segundo Valor '))
opcao = 0
while opcao !=5:
    print('''
      
    [1-Somar]
    [2-Multiplicar]
    [3-Maior]
    [4-Novos Numeros]
    [5-Sair do Programa]''')
    
    opcao = int(input('Digite a Opção Desejada '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} = {soma}')
    elif opcao == 2:
        produto = n1*n2
        print(f'O Produto entre {n1} e {n2} = {produto}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior entre {n1} e {n2} é {n1}')
        elif n2 > n1:
            print(f'O maior entre {n1} e {n2} é {n2}')
        else:
            print('Os dois valores são iguais!')
        
    elif opcao == 4:
        print('Informe os valores novamente')
        n1 = int(input('Primeiro Valor '))
        n2 = int(input('Segundo Valor '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção Invalida! tente Novamente')
    print('-=-'* 10)    
    sleep(2)
print('Fim do Programa!Volte Sempre!')



            

    
                
