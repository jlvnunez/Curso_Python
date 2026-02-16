#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

print('Detector de Palindromo Sem o for')
print('=' *20)

frase = str(input('Digite uma frase ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
#inverso =''
'''for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]'''
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um PALINDROMO')
else:
    print('A frase digitada NÂO É UM PALINDROMO')
