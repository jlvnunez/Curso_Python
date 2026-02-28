#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for _ in range(0,5):
    n = int(input('Digite um valor: '))
    
    # Se a lista estiver vazia ou o número for maior que o último, apenas adiciona
    if not lista or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final...')
    else:
        # Percorre a lista e insere no primeiro momento em que o número for menor
        for i, valor in enumerate(lista):
            if n <= valor:
                lista.insert(i, n)
                print(f'Adicionado na posição {i}...')
                break

print('-' * 30)
print(f'Lista ordenada: {lista}')

'''Por que esta versão é mais simples?
if not lista: Em Python, uma lista vazia é considerada "Falsa". Usar if not lista é mais direto que checar o contador do loop.

enumerate(lista): Esta função é fantástica. Ela te entrega o índice (i) e o conteúdo (valor) ao mesmo tempo. Isso elimina a necessidade de criar uma variável pos = 0 e ficar somando +1 manualmente.

Menos linhas: A lógica fica contida dentro de um bloco mais legível.

Visualizando a Inserção
O que o código faz é basicamente o conceito de Insertion Sort. Imagine organizar uma mão de cartas de baralho: você pega uma carta nova e percorre as que já estão na sua mão até encontrar o lugar dela.

Dica de Pythonista: O _ no for _ in range(5) é uma convenção usada quando você não precisa utilizar a variável do contador dentro do loop.'''

