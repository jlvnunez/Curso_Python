#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

cont = 0
soma = 0
for c in range(1,7):
    num = int(input(f'Digite o {c}° numero: '))
    if num %2==0:
        cont += 1  #e igual cont = cont+1
        soma += num #e igual soma = soma+num

print()
print(f'Voce informou {cont} numeros PARES e a soma deles foram {soma}\n')   

input('Digite enter para encerrar...')    
