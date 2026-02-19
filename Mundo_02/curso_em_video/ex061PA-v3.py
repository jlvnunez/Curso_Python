#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('=' * 22)
print('PA com Regra do 10º Termo')
print('=' * 22)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

# Aqui usamos a sua fórmula matemática
decimo = primeiro + (10 - 1) * razao

termo = primeiro

# O loop para assim que ultrapassar o valor do décimo termo
while termo <= decimo:
    print(f'{termo} ', end='→ ')
    termo += razao

print('ACABOU')
     

