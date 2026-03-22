#Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

#programa principal
import moeda
p= float(input('Digite o Preço R$ '))
print(f'A metade de  {moeda.moeda(p)} é:  {moeda.metade(p,True)}')
print(f'O dobro de  {moeda.moeda(p)} é  {moeda.dobro(p,True)}')
print(f'Aumentando 10% de {moeda.moeda(p)},temos R$ {moeda.aumentar(p,10,True)}')
print(f'Com desconto de 20% de {moeda.moeda(p)},temos {moeda.diminuir(p,20,True)}')