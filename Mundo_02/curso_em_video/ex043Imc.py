#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
import os
os.system("")# Esse comando "limpa" o terminal e ativa o suporte a cores ANSI no Windows

print('*' *30)
print('Calculadora IMC(Indice de Massa Corpôrea)')
print('*' *30)
print('''Tabela IMC
- IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida ''')
print('*' *30)

peso =float(input('Digite seu peso '))
altura = float(input('Digite sua altura(em Metros) '))
imc = peso /(altura**2)
print(f'Seu IMC é de {imc:.1f}')

if imc < 18.5:
    print('Voce esta ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('Voce esta no PESO IDEAL')
elif imc >= 25 and imc <= 30:
    print('Voce esta com SOBREPESO')
elif imc >30 and imc <= 40:
    print('Voce esta OBESO')
else:
    print('Voce esta com OBESIDADE MÓRBIDA')

input('Clique enter para encerrar...')