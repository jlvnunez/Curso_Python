#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
from datetime import date
print('-=-' *20)
print('       CLASSIFICAÇÃO DE ATLETAS')
print('''– Até 9 anos:MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos:MASTER''')
print('-=-' *20)

nasc = int(input('Ano de Nascimento '))
atual = date.today().year
idade = atual - nasc
print(f'O atleta tem {idade} anos')


if idade < 0:
    print('\033[31mErro: O ano de nascimento não pode ser maior que o ano atual!\033[m')
elif idade >= 120:
    print('\033[31mErro: Verifique o ano digitado. Idade acima do limite esperado.\033[m')
else:
     if idade <= 9:
        print('Classificação MIRIM')
     elif idade <= 14:
        print('Classificação INFANTIL')
     elif idade <= 19:
        print('Classificação JUNIOR')
     elif idade <= 25:
        print('Classificação SENIOR')
     else:
        print('Classificação MASTER')


    

    



