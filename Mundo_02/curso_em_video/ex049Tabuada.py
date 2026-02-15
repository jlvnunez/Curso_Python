#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
#cont = 0
print('\033[34m=\033[m' * 30)
n = int(input('Digite um Numero:  '))
print(f'Voce Escolheu a Tabuada do {n}')
print('\033[34m=\033[m' * 30)
for cont in range(1,11):
    resultado = n * cont
    print(f'{n} x \033[32m{cont:2}\033[m = \033[1;36m{resultado}\033[m') 

print('\033[34m=\033[m' * 30)
    