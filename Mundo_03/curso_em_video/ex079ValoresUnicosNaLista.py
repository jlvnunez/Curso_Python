#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros =[]

while True:
    n= int(input('Digite um Valor '))
    if n not in numeros:
        numeros.append(n)
        print('Numero Adicionado com sucesso!')
    else:
         print('O numero Ja existe,não posso adicionar!')

    resp = str(input('Quer continuar?[S/N] ')).strip().upper()
      
    if resp == 'N':
        break
print('-=' * 20)
print(f'Voce digitou a sequencia de: {numeros}')
print(f'Os valores em ordem crescente são: {sorted(numeros)}')
    
