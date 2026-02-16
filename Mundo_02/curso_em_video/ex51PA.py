#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('progressao Aritimetica')
print('=' *25)

primeiroTermo = int(input('Digite o primeiro termo '))
razao = int(input('Digite a razao '))
decimo = primeiroTermo +(10-1)*razao

for c in range(primeiroTermo,decimo + razao,razao):
    print(f'{c}',end = ' -> ')
print('ACABOU!!!!')    