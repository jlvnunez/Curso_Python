#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp ='S'
soma = quant = media = maior = menor =0
while resp in 'Ss':
    n = int(input('Digite um numero '))
    soma += n
    quant +=1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n 
        if n < menor:
            menor = n

    resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]  
media = soma / quant
print(f'Voce digitou {quant} numeros e a media foi {media} ')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
     
    