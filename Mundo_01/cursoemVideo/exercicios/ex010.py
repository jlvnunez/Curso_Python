#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

dinheiro = float(input('Quanto dinheiro voce tem na carteira? '))
cotacao= float(input('qual a cotacao do dolar atual '))
conversao= dinheiro/cotacao
print(f'Cotacao atual do dolar {cotacao}.\nCom R$ {dinheiro:.2f} reais,voce consegue comprar $ {conversao:.2f} dolares')