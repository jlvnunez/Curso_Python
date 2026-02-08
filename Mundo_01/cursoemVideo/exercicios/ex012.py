#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de 
#desconto.
preco = float(input('digite o preco do produto '))
percentual = preco *(5/100)
preconovo= preco-percentual
print(f'O valor do produto é de R$ {preco:.2f} \n Com o desconto de 5% , ele passa a custar R$ {preconovo:.2f}')
 