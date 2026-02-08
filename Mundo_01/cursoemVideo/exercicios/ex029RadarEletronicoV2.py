#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
LIMITE = 80
VALOR_POR_KM = 7

print('=' * 40)
print(f'{"RADAR ELETRÔNICO":^40}') #:^40: Centraliza o texto em um espaço de 40 caracteres.
print('=' * 40)

velocidade = float(input('Qual a velocidade atual do carro? '))

if velocidade <= LIMITE:
    print('\033[32mBoa viagem! Dirija com segurança.\033[m')
else:
    print('\033[31mMULTADO! Você excedeu o limite de 80Km/h.\033[m')
    multa = (velocidade - LIMITE) * VALOR_POR_KM
    print(f'O valor da multa é de R${multa:.2f}')