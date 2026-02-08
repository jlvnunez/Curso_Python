#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('=' * 54)
print('Baseando em R$60,00 de diaria e R$ 0,15 por km rodado')
print('=' * 54)
# Entrada de dados
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

# Cálculo do preço
# R$ 60,00 por dia e R$ 0,15 por km
preco_total = (dias * 60) + (km * 0.15)

# Exibição do resultado
print(f'O total a pagar é de R${preco_total:.2f}')