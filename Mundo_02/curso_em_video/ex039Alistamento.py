#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
print('*' *42)
from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Voce tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Ainda faltam {saldo} {"ano" if saldo == 1 else "anos"}  para se alistar')
    print(f'Seu alistamento deve ser no ano de {ano}')
else:
     saldo = idade -18
     ano = atual - saldo
     print(f'Voce ja deveria ter se alistado há {saldo} {"ano" if saldo == 1 else "anos"} ')
     print(f'Seu alistamento deveria ter sido em {ano}')

print('*' *42)

input('Clique enter para encerrar...')



