#Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

#programa principal
import moeda
p= float(input('Digite o Preço R$ '))
print(f'A metade de  {moeda.moeda(p)} é:  {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de  {moeda.moeda(p)} é  {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% de {moeda.moeda(p)},temos R$ {moeda.moeda(moeda.aumentar(p,10))}')
print(f'Com desconto de 20% de {moeda.moeda(p)},temos  {moeda.moeda(moeda.diminuir(p,20))}')