#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    print('-' * 25)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 25)

    # 1. Condição de Parada (Flag)
    if n < 0:
        break

    # 2. Reiniciar o contador para a nova tabuada
    cont = 1 

    # 3. Loop interno para calcular de 1 a 10
    while cont <= 10:
        resultado = n * cont
        print(f'{n} x {cont:2} = {resultado}')
        cont += 1  # Incrementa o contador para não virar loop infinito

print('\033[1;31mPROGRAMA TABUADA ENCERRADO. Volte sempre!\033[m')