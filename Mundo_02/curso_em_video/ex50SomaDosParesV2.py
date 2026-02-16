#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

# 1. Perguntamos ao usuário o limite

total_numeros = int(input('Quantos números você deseja digitar? '))
cont = 0
soma = 0

# 2. O range agora vai de 1 até (total_numeros + 1)
for c in range(1, total_numeros +1 ):
    num = int(input(f'Digite o {c}° número: '))
    if num % 2 == 0:
        cont += 1
        soma += num

print() # Pula a linha como você queria
print(f'Você informou {cont} números PARES e a soma deles foi {soma}')
input('\nDigite enter para encerrar...')
