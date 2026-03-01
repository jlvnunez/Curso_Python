#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
print('='*45) 
print('LISTA ORDENADA V1.0')
print('='*45) 
lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    
    # Caso 1: Se for o primeiro número ou maior que o último da lista
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    
    # Caso 2: Procurar a posição correta para inserir
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print('-' * 30)
print(f'Os valores digitados em ordem foram: {lista}')
