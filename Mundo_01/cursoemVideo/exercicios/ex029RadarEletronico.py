#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
print('=' *50)
print('Velocidade maxima permitida 80km/h')
print('O valor da multa será R$7,00 por km acima do limite')
print('=' *50)
velocidade = float(input('Digite a velocidade do carro '))
print(f'Sua velocidade e de {velocidade} km/h')

if velocidade <= 80:
    print('Voce esta dentro da velocidade permitida')
else:
    print('Limite de velocidade excedido,voce será Multado!')
    multa = (velocidade -80)* 7
    print(f'A multa irá custar {multa:.2f} reais')