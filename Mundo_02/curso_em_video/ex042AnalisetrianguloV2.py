#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
import os
os.system("")# Esse comando "limpa" o terminal e ativa o suporte a cores ANSI no Windows

print('-=-' *15)
print('Analisando se forma um Triangulo')
print('-=-' *15)
r1 = float(input('Digite o primeiro segmento '))
r2 = float(input('Digite o segundo segmento '))
r3 = float(input('Digite o terceiro segmento '))
print('-=-' *15)

if r1+r2 > r3 and r1+r3 > r2 and r2+r3 > r1:
    print('Os segmentos \033[1;36mPODEM FORMAR\033[m um triângulo ' )
    
    if r1 == r2 == r3: 
        print('\033[1;32mEsses Valores formam um Triangulo Equilatero\033[m') 
    elif r1 != r2 !=r3 != r1: 
        print('\033[1;32mEsses Valores formam um Triangulo Escaleno\033[m')
    else:
        print('\033[1;32mEsse Valores formam um Triangulo Isoceles\033[m')

else:
    print('Os segmentos \033[1;31mNÃO PODEM FORMAR\033[m um triângulo!')

input('Clique enter para encerrar...')


