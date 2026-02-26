#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
print()
print(f'{"Contando Vogais em Tupla":=^40}')
palavras =('fruta','mundo','computador','amanhecer','juventude',
           'python','amendoim','aprendizado')

for p in palavras:
    print(f'\nNa palavra {p.upper()},temos:',end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'\033[1;31m{letra}\033[m',end='  ')
print('\n' + '-' * 40)

