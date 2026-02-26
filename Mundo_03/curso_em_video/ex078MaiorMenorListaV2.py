#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []

# Coleta de dados
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))

# Uso de funções nativas (mais rápido e legível)
maior = max(lista)
menor = min(lista)

print('-=' * 20)
print(f'Você digitou os valores: {lista}')

# Exibição do Maior
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print()

# Exibição do Menor
print(f'O menor valor digitado foi {menor} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
print()


    
    
    