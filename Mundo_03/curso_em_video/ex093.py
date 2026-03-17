#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


print(f'{"Cadastro de Jogadores Versao 1.0":=^50}')
jogador={}
partidas=[]
jogador['nome']=str(input('Nome Jogador '))
tot= int(input(f'Total de partidas de {jogador['nome']} '))
for c in range (0,tot):
    partidas.append(int(input(f' Quantos gol na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total']= sum(partidas)
print('='*50)
print(jogador)
print('='*50)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor de {v}')
print('='*50)
print(f' O Jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas')
for i ,v in enumerate(jogador['gols']):
    print(f'  ==> Na partida {i+1} fez {v} gols')
print(f'Foi um total de {jogador['total']} gols')
