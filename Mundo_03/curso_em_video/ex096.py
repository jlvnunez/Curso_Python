#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg,compr):
    a= larg * compr
    print(f' A area do terreno de {larg} x {compr} é de: {a} m2') 

#programa principal
print('='*30) 
print("Controle de Terrenos")   
print('='*30)    
l=float(input('Largura em (m): '))
c= float(input("Comprimenro em (m): "))
area(l,c)

