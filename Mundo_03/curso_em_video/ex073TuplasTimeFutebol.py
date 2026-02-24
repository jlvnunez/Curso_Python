#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
'''
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
print(f'{" TABELA DO BRASILEIRÃO 2026 ":=^80}')
times=('Palmeiras','Sao Paulo','Fluminense','Bahia','Corinthians','Athletico-PR','Bragantino','Chapecoense','Mirassol','Coritiba','Flamengo','Botafofo','Gremio','Vitoria','Atletico MG','Remo','Vasco','Santos','Internacional','Cruzeiro' )

print(f'Os 5 primeiros times: {times[0:5]}')
print('=' *80)
print(f'Os ultimos 4 colocados: {times[-4:]}')
print('=' *80)
print(f'Times em ordem Alfabetica: {sorted(times)}')
print('=' *80)
posicao = times.index('Chapecoense')+1
print(f'A Chapecoense esta na {posicao}ª posição')
print('=' *80)