#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
print('*' * 30)
print('Calculadora IMC')
print('*' * 30)

# Lendo como texto primeiro para tratar a vírgula
peso_input = input('Digite seu peso (kg): ').replace(',', '.')
altura_input = input('Digite sua altura: ').replace(',', '.')

peso = float(peso_input)
altura = float(altura_input)

# Se o usuário digitou em centímetros (ex: 170 em vez de 1.70)
if altura > 3:
    altura = altura / 100

imc = peso / (altura ** 2)
print(f'\nSeu IMC é de {imc:.1f}')

# Lógica de Classificação
if imc < 18.5:
    status = '\033[1;33mABAIXO DO PESO\033[m'
elif imc < 25:
    status = '\033[1;32mPESO IDEAL\033[m'
elif imc < 30:
    status = '\033[1;33mSOBREPESO\033[m'
elif imc <= 40:
    status = '\033[1;31mOBESO\033[m'
else:
    status = '\033[1;31;40mOBESIDADE MÓRBIDA\033[m'

print(f'Você está: {status}')