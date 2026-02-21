#Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
n= cont = soma =0
while True:
    try:
        n= int(input('Digite um Numero inteiro '))

    except ValueError:
        print('❌\033[1;31mErro! Por favor, digite apenas números inteiros.\033[m')
        continue
    if n == 999:
       break
    soma += n
    cont += 1
    media = soma / cont
print(f'\033[1;32mVoce digitou {cont} numeros e a soma entre eles é {soma}\033[m')

 