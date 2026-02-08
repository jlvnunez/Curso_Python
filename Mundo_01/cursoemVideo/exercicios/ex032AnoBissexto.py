#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime
print('='*30)
ano = int(input('Que ano voce quer analisar? Digite "0"para Analisar ano atual '))
if ano == 0:
    ano = datetime.date.today().year
    
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print(f'O ano {ano} é \033[32mBISSEXTO\033[m!')
else:
        print(f'O ano {ano} não é \033[32mBISSEXTO\033[m!')
print('=' *30)




