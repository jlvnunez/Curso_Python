#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
print('==='*10)
print('Menor e Maior Peso Versao 2.0')
print('==='*10)
pesos = [] # Criamos uma lista vazia

for p in range(1, 6):
    # Adicionamos o peso digitado direto na lista usando o .append()
    pesos.append(float(input(f'Peso da {p}ª pessoa: ')))

# Usamos as funções prontas do Python: max() e min()
print(f'O maior peso lido foi {max(pesos)}kg')
print(f'O menor peso lido foi {min(pesos)}kg')
print()
input('digite enter para encerrar...')
    

'''O que mudou aqui?
-pesos = []: Inicializa uma lista vazia.
-.append(): É o comando que "empurra" um novo valor para o final da lista.
-max(pesos): Vasculha a lista inteira e retorna o maior número.
-min(pesos): Vasculha a lista inteira e retorna o menor número.'''
    

