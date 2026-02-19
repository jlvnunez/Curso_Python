#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('=' * 25)
print('Gerador de PA Customizado')
print('=' * 25)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
n = int(input('Quantos termos você quer ver? ')) # Aqui o usuário define o "n"

# Calculando o enésimo termo (o limite final)
enesimo_termo = primeiro + (n - 1) * razao

termo_atual = primeiro

print(f'\nExibindo os {n} primeiros termos:')

# O loop continua enquanto não ultrapassar o valor do enésimo termo
while termo_atual <= enesimo_termo:
    print(f'{termo_atual}', end=' → ')
    termo_atual += razao

print('FIM')
     

