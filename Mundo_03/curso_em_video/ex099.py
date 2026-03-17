#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
print(f'{"Função que descobre o Maior":=^50}')

from time import sleep
def maior(* num):
    cont=maior=0
    print('-=' *30)
    print('\nAnalisando os parametros passados')
    for valor in num:
        print(f'{valor} ',end='',flush=True)
        sleep(0.3)
        if cont ==0:
            maior=valor
        else:
            if valor > maior:
                maior=valor
        cont +=1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O MAIOR valor informado foi {maior}')
#programa principal
maior(2,5,30,9,20,16)
maior(1,5,6,2,0)
maior(100,30,45,1)
maior(6)
maior()