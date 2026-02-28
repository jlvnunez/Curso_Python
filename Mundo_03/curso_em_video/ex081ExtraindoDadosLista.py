#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:      
# A)Quantos números foram digitados.                                                                       B) A lista de valores, ordenada de forma decrescente.                                                                   C) Se o valor 5 foi digitado e está ou não na lista.    
print('='*45) 
print('EXTRAINDO DADOS DE UMA LISTA')
print('='*45) 
numeros=[]
while True :
    numeros.append(int(input('Digite um numero  ')))
    resp=str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('='*45)    
print(f'A)Voce digitou {len(numeros)} elementos') #len(valores) para saber numero de elementos
numeros.sort(reverse=True)
print(f'B)Os numeros em ordem decrescente: {numeros} ')
if 5 in numeros:
    print('C)O valor 5 faz parte da lista')
else:
    print('C)O valor 5 nao faz parte da lista')

print('='*45)   