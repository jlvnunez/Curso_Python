#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import random
from time import sleep

print('-' * 30)
print(f'{"PALPITES MEGA SENA V3.0":^30}')
print('-' * 30)

quant = int(input('Quantos jogos você quer sortear? '))
jogos = []

for i in range(quant):
    # random.sample(população, k) escolhe k itens ÚNICOS de uma vez
    bilhete = random.sample(range(1, 61), 6)
    bilhete.sort()
    jogos.append(bilhete)

print(f'\n-=-=-= SORTEANDO {quant} JOGOS =-=-=-')
for indice, jogo in enumerate(jogos):
    sleep(0.5)
    print(f'Jogo {indice + 1}: {jogo}')

print('-' * 10, '< BOA SORTE! >', '-' * 10)

import random
from time import sleep

print('-' * 30)
print(f'{"PALPITES MEGA SENA":^30}')
print('-' * 30)

quant = int(input('Quantos jogos você quer sortear? '))
jogos = []

for i in range(quant):
    # random.sample(população, k) escolhe k itens ÚNICOS de uma vez
    bilhete = random.sample(range(1, 61), 6)
    bilhete.sort()
    jogos.append(bilhete)

print(f'\n-=-=-= SORTEANDO {quant} JOGOS =-=-=-')
for indice, jogo in enumerate(jogos):
    sleep(0.5)
    print(f'Jogo {indice + 1}: {jogo}')

print('-' * 10, '< BOA SORTE! >', '-' * 10)


'''Por que esta forma é melhor?

>random.sample(range(1, 61), 6): Esta única linha substitui todo aquele bloco de "sorteia, vê se já existe, adiciona, conta até 6". Ela já garante que os 6 números sejam diferentes entre si.

>range(quant): O for é mais direto que o while quando você já sabe exatamente quantas vezes quer repetir (a quantidade de jogos).

>Legibilidade: O código fica muito mais limpo e menos propenso a erros de lógica.

Resumo Comparativo

Característica	Método Manual (while)	             Método random.sample
Complexidade	Média (exige controle de duplicatas)	Baixa (automático)
Linhas de Código	~    20-25	                            ~10-12
Risco de Loop Infinito	Existe (se errar o contador)	Inexistente '''