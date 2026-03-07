#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

print(f'{"Jogos de Dados em Python":=^50}')

from random import randint
from time import sleep
from operator import itemgetter
jogo={'Jogador 1':randint(1,6),
      'Jogador 2':randint(1,6),
      'Jogador 3':randint(1,6),
      'Jogador 4':randint(1,6)}
ranking=[]
print('Jogos sorteados:')
for k,v in jogo.items():
    print(f'{k} Tirou {v} no Dado')
    sleep(1)
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True)    
print('='*50)
print(f'{"Ranking dos Jogadores":=^50}')
for i,v in enumerate(ranking):
    print(f'{i+1}° lugar {v[0]} com {v[1]}')

input('ENTER PARA FINALIZAR...')


