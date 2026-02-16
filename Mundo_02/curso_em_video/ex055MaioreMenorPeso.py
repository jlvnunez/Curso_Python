#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
print('==='*10)
print('Menor e Maior Peso Versao 1.0')
print('==='*10)
maiorPeso = 0
menorPeso = 0

for pessoa in range(1, 6):
    peso = float(input(f'Digite o peso da {pessoa}ª Pessoa: '))
    
    if pessoa == 1:
        menorPeso = peso
        maiorPeso = peso
    else:
        # Verifica se é o novo maior
        if peso > maiorPeso:
            maiorPeso = peso
        
        # Verifica se é o novo menor (independente de ser maior ou não)
        if peso < menorPeso:
            menorPeso = peso

print('==='*10)

print(f'O Menor peso lido foi: {menorPeso}kg')
print(f'O Maior peso lido foi: {maiorPeso}kg')
    
    

