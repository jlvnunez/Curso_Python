#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

print('-='*20)
print("     Ficha Jogador -Criar Função     ")
print('-='*20)
def ficha(jog='desconhecido',gol=0):
    print(f'O Jogador {jog} fez {gol} gol(s) no campeonato')

#programa principal
n =str(input('Nome Jogador: '))
g =str(input('quantidade de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g=0
if n.strip() =='':
    ficha(gol=g)
else:
    ficha(n,g)

