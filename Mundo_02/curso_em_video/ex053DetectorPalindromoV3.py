#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# Passo 1: Ler a frase e tratar os dados
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # Divide a frase em uma lista de palavras
junto = ''.join(palavras) # Junta tudo sem espaços
inverso = ''

# Passo 2: Usar o 'for' para inverter a string
# Vamos percorrer do índice da última letra até o primeiro (0)
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f'O inverso de {junto} é \033[1;32m{inverso}.\033[m')

# Passo 3: Verificação final
if inverso == junto:
    print('\033[1;32mTemos um palíndromo!\033[m')
else:
    print('\033[1;31mA frase digitada não é um palíndromo.\033[m')

    '''Por que usamos esses números no range?
Para inverter a palavra com o for, precisamos "contar para trás". Imagine a palavra "ANA":

len(junto) - 1: Começamos na última posição (índice 2).

-1: Queremos parar antes do -1, ou seja, no índice 0.

-1: É o "passo" (step), indicando que vamos subtrair 1 a cada volta.

Dica de Ouro (Python Style)
Embora o exercício peça o uso do for, no dia a dia do Python costumamos fazer isso de forma muito mais simples usando fatiamento de strings (slicing):

Python
inverso = junto[::-1] # Isso faz exatamente o mesmo que o bloco 'for' acima!'''
