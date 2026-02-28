#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

# Gerando a tupla de forma dinâmica
numeros = tuple(randint(1, 10) for _ in range(5))

print(f'Os valores sorteados foram: ', end='')
print(*numeros) # Forma simplificada de imprimir

# Usando funções nativas para análise
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')