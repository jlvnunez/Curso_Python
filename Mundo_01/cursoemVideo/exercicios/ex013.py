#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o valor do salario '))
percentual = salario *(15/100)
novosalario = salario + percentual
print(f'O salario atual e de R$ {salario:.2f} reais\nCom o aumento de 15%,o funcionario passará a receber o valor de R$ {novosalario:.2f} reais')


