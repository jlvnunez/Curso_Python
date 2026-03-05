#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import random
from time import sleep

# Cabeçalho estilizado
print('-' * 30)
print(f'{"JOGA NA MEGA SENA V2.0":^30}')
print('-' * 30)

lista_jogos = []
dados_jogo = []

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total_jogos = 1

while total_jogos <= quantidade:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in dados_jogo:
            dados_jogo.append(num)
            cont += 1
        if cont >= 6:
            break
            
    dados_jogo.sort()
    lista_jogos.append(dados_jogo[:]) # Cria uma cópia da lista
    dados_jogo.clear()
    total_jogos += 1

# Exibição dos resultados
print('-=' * 3, f' SORTEANDO {quantidade} JOGOS ', '=-' * 3)
for i, jogo in enumerate(lista_jogos):
    print(f'Jogo {i+1}: {jogo}')
    sleep(0.5) # Efeito dramático de carregamento

print('-=' * 5, '< BOA SORTE! >', '=-' * 5)


'''💡 O que está acontecendo no código:
random.randint(1, 60): Sorteia números inteiros dentro do intervalo oficial da Mega Sena.

if num not in dados_jogo: Esta é a validação crucial. Ela garante que o programa não adicione o mesmo número duas vezes no mesmo jogo.

lista_jogos.append(dados_jogo[:] ): Usamos [:] para criar uma cópia (fatiamento completo). Se você apenas der o append, ao limpar a lista dados_jogo com o .clear(), os dados dentro da lista principal também sumiriam por causa da ligação de memória.

enumerate(): Facilitamos a exibição para mostrar "Jogo 1", "Jogo 2", etc.'''