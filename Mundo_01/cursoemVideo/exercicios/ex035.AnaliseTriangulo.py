#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=-' *15)
print('Analisando se forma um Triangulo')
print('-=-' *15)
r1 = float(input('Digite o primeiro segmento '))
r2 = float(input('Digite o segundo segmento '))
r3 = float(input('Digite o terceiro segmento '))
print('-=-' *15)

if r1+r2 > r3 and r1+r3 > r2 and r2+r3 > r1:
    print('Os segmentos \033[32mPODEM FORMAR\033[m um triângulo ' )
else:
    print('Os segmentos \033[31mNÃO PODEM FORMAR\033[m um triângulo!')

