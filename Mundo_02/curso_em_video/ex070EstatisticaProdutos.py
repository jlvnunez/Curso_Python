#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
'''A) qual é o total gasto na compra.
   B) quantos produtos custam mais de R$1000.
   C) qual é o nome do produto mais barato.'''
print(f'{" ESTATISTICA EM PRODUTOS ":=^40}')  
cont=total=maiorquemil=menorPreco =0
barato = ' '
while True:
    prod = str(input('Nome do Produto '))
    preco = float(input('Valor '))
    cont+= 1
    total += preco
    
    if preco > 1000:
         maiorquemil+= 1

    if cont ==1 or preco < menorPreco:
         menorPreco=preco
         barato = prod
         
    
    resp =' '
    while resp not in 'SN':
      resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
            break
print('=' * 40)     

print(f'Total Gasto na compra {total:.2f}')
print(f'Temos {maiorquemil} produtos custando mais de R$1000,00')
print(f'O produto mais bararto foi {barato} que custou R$ {menorPreco:.2f}')
print(f'{" FIM DO PROGRAMA ":=^40}')      


