#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: 
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2  
#c)uma contagem personalizada
from time import sleep
print('Função de Contador')
print()
def contador(inicio,fim,passo):
    if passo < 0:
        passo *= -1
    if passo ==0:
        passo=1
    print('-='*20)
    print(f'Contagem de {inicio} em {fim} de {passo} em {passo}')
    #sleep(2.5)

    if inicio < fim:
        cont= inicio
        while cont <= fim:
            print(f'{cont} ',end='', flush=True)
            sleep(0.2)
            cont+= passo
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ',end='',flush=True)
            sleep(0.2)
            cont -= passo
        print("FIM")    

contador(1,10,1) 
contador(10,0,2)  
print('-='*20)
print('Contagem Personalizada') 
i= int(input('Inicio: '))
f= int(input('Fim: '))
p= int(input('Passos: '))
contador(i,f,p)