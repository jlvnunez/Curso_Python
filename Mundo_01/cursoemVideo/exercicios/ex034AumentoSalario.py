#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
print('=' *40)
salario = float(input('Qual e o salario do funcionario? '))
print('=' *40)
if salario > 1250:
    novoSalario = salario * 1.10
else:
    novoSalario = salario * 1.15
 
print(f'O salario atual do funcionario é {salario:.2f}')    
print(f'Com o aumento, o funcionario passara a receber: R$ {novoSalario:.2f}')
print('=' *40)
