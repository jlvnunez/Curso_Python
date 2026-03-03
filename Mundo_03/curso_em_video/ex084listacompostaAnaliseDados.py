'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No Final mostre:                                                               
A) Quantas pessoas foram cadastradas.
B)Uma listagem com as pessoas mais pesadas.
C)Uma listagem com as pessoas mais leves.'''
print('=-'*25)                                                            
print(f'{"Lista Composta e Analise de Dados":^50}')
print('=-'*25) 

temp=[] #lista temporaria
principal=[]  #lista principal
maior=menor=0
while True:
    temp.append(str(input('Nome ')))
    temp.append(float(input('Peso ')))
    if len(principal)==0:
        maior=menor=temp[1]
    if temp[1] > maior:
        maior = temp[1]
    if temp[1] < menor:
        menor = temp[1]

    principal.append(temp[:])
    temp.clear()

    resp=str(input('Quer continuar?[S/N] '))
    if resp in 'Nn':
        break
print('=-'*25) 
print(f'Dados Cadastrados: {principal}')
print(f'A)Ao todo foram cadastrados {len(principal)} pessoas.' )
print(f'B)Listagem pessoas + pesadas {maior}Kg.Peso de ',end='')
for p in principal:
    if p[1]== maior:
        print(f'[{p[0]}]',end='')
print()
print(f'B)Listagem pessoas + leves {menor}Kg .Peso de ',end='')
for p in principal:
    if p[1]==menor:
        print(f'[{p[0]}]',end='')



