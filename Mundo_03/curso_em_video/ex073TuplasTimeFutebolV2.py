#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
'''
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
times = ('Palmeiras', 'São Paulo', 'Fluminense', 'Bahia', 'Corinthians',
         'Athletico-PR', 'Bragantino', 'Chapecoense', 'Mirassol','Coritiba',
         'Flamengo','Botafogo','Grêmio','Vitória','Atlético-MG',
         'Remo','Vasco','Santos','Internacional','Cruzeiro')

# Título usando o que aprendemos antes
print(f'{" TABELA DO BRASILEIRÃO 2026 ":=^80}')
for posicao,time in enumerate(times):
    print(f'{posicao +1}° - {time}')
print('=' * 120)
# Exibindo os 5 primeiros de forma limpa
print(f'Os 5 primeiros times: {", ".join(times[0:5])}')
print('=' * 150)

# Exibindo os 4 últimos
print(f'Os últimos 4 colocados: \033[1;31m{", ".join(times[-4:])}\033[m')
print('=' * 100)

# Ordem alfabética (sorted retorna uma lista, então o join funciona igual)
print(f'Times em ordem Alfabética: {", ".join(sorted(times))}')
print('=' * 100)

# Posição específica
posicao = times.index('Chapecoense') + 1
print(f'A Chapecoense está na {posicao}ª posição')
print('=' * 100)