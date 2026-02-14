#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

import os
os.system("")# Esse comando "limpa" o terminal e ativa o suporte a cores ANSI no Windows

print('='*10, ' LOJAS JLVNUNEZ ', '='*10)
preco = float(input('Preço das compras: R$ '))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco * 0.90
    print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
elif opcao == 2:
    total = preco * 0.95
    print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.')
elif opcao == 4:
    total = preco * 1.20
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS.')
    print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
else:
    print('\033[31mOPÇÃO INVÁLIDA de pagamento. Tente novamente!\033[m')

input('Clique enter para encerrar...')