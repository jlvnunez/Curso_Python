#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
print('=' *50)
salario = float(input('Qual e o salario do funcionario? '))
print('=' *50)
if salario > 1250:
   percentual = 10 
   aumento = (salario*percentual) /100 
   salario += aumento
else:
    percentual = 15
    aumento = (salario * percentual) /100
    salario += aumento
 
print(f'O salario atual do funcionario é de R$ {salario:.2f} Reais')    
print(f'Com o aumento de {percentual}%, o funcionario passara a receber: R$ {salario:.2f}')
print('=' *50)
