#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorImovel = float(input('Digite o Valor do imovel '))
valorSalario = float(input('Digite valor do salario '))
anos = int(input('Em quantos anos pretende pagar? '))

meses = anos*12
prestacao = valorImovel / meses
limite = valorSalario * 0.30
print('-=-'*15)
print(f'Para pagar um imovel no valor de R$ {valorImovel:.2f} em {anos} anos')
print(f'a prestacao será de R$ {prestacao:.2f}')

if prestacao <= limite:
    print('\033[32mEMPRESTIMO CONCEDIDO!!\033[m')
else:
    print('\033[31mEMPRESTIMO NEGADO!!\033[m')
    print(f'O valor da parcela excede 30% do seu Salario (R$ {limite:.2f})')