#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
'''
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
# Tupla com os times (mantendo sua lista original)
times = ('Palmeiras', 'Sao Paulo', 'Fluminense', 'Bahia', 'Corinthians',
         'Athletico-PR', 'Bragantino', 'Chapecoense', 'Mirassol', 'Coritiba',
         'Flamengo', 'Botafogo', 'Gremio', 'Vitoria', 'Atletico MG',
         'Remo', 'Vasco', 'Santos', 'Internacional', 'Cruzeiro')

# 1. Cabeçalho Centralizado
print(f'{" TABELA DO BRASILEIRÃO 2026 ":=^50}')

# 2. Impressão da Tabela com Cores (G4 em Azul e Z4 em Vermelho)
for i, time in enumerate(times):
    pos = i + 1
    # Destaque para o G4 (Libertadores)
    if pos <= 6:
        print(f'\033[1;32m{pos:>2}º - {time}\033[m')
    # Destaque para o Z4 (Rebaixamento)
    elif pos >= 17:
        print(f'\033[1;31m{pos:>2}º - {time}\033[m')
    # Demais times
    else:
        print(f'{pos:>2}º - {time}')

print('=' * 50)

# 3. Análises solicitadas no exercício
# a) Os 5 primeiros
print(f'A) Os 6 primeiros são: \033[1;32m{", ".join(times[:6])}\033[m')

# b) Os últimos 4
print(f'B) Os 4 últimos (Z4): \033[1;31m{", ".join(times[-4:])}\033[m')

# c) Ordem Alfabética
print(f'C) Times em ordem alfabética: {", ".join(sorted(times))}')

# d) Posição da Chapecoense
try:
    busca = 'Chapecoense'
    pos_chape = times.index(busca) + 1
    print(f'D) O {busca} está na \033[1;33m{pos_chape}ª\033[m posição.')
except ValueError:
    print(f'D) O time {busca} não foi encontrado na tabela.')

print(f'{" PROGRAMA ENCERRADO ":=^50}')