#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

#programa principal
import moeda

p= float(input('Digite o Preço R$ '))
print(f'A metade de R$ {p} é: R$ {moeda.metade(p)}')
print(f'O dobro de R$ {p} é R$ {moeda.dobro(p)}')
print(f'Aumentando 10% de R$ {p},temos R$ {moeda.aumentar(p,10)}')
print(f'Com desconto de 20% de R$ {p},temos R$ {moeda.diminuir(p,20)}')