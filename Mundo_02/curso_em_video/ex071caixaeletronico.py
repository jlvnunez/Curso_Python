#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS
#--considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor= int(input('Quanto voce quer Sacar? '))
total = valor
cedula = 50
total_cedulas =0

while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R$ {cedula:.2f}')
# Lógica para trocar o valor da cédula atual
        if cedula == 50:
            cedula=20
        elif cedula==20:
            cedula = 10
        elif cedula == 10:
            cedula =1
# Reseta o contador para a próxima nota
        total_cedulas=0
        if total ==0:
            break

print('=' * 30)
print('Saque realizado com sucesso. Volte sempre!')

#estudos da logica:
'''Como a lógica funciona:Variáveis de Controle: Começamos definindo a cédula de maior valor (R$50) e um contador de quantas notas serão entregues.O Loop while: O programa tenta tirar o valor da nota atual do montante total o máximo de vezes possível.A Transição: Quando o valor restante é menor que a nota atual (ex: sobrou R$15 e a nota é de R$20), o programa imprime o resultado da nota anterior e "pula" para a próxima nota disponível na sequência (50 -> 20 -> 10 -> 1).Condição de Parada: O loop encerra assim que o total a ser sacado chega a zero.Dica de Ouro: Note que usamos total_cedulas > 0 antes de imprimir. Isso evita que o programa diga que vai entregar "0 cédulas de R$20" caso o valor do saque não precise dessa nota específica. '''

