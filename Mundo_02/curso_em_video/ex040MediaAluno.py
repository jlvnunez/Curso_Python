#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
import os
os.system("")# Esse comando "limpa" o terminal e ativa o suporte a cores ANSI no Windows
print('*' *35)
print('– Média 7.0 ou superior: APROVADO\n– Média entre 5.0 e 6.9: RECUPERAÇÃO\n– Média abaixo de 5.0: REPROVADO')
print('*' *35)
n1=float(input('Digite a Primeira Nota '))
n2=float(input('Digite a segunda nota '))
media = (n1+n2)/2
print(f'Notas Obtidas:\nprimeira nota: {n1}\nsegunda nota: {n2}')
print(f'A media obtida foi: {media:.1f}')

if media >=7:
  print('\033[1;32mAluno Aprovado\033[m')
elif media >= 5 and media <= 6.9: # ou elif 5 <= media < 7:
  print('\033[1;33mAluno em recuperação\033[m')
else:
  print('\033[1;31mAluno reprovado\033[m')

input('aperte o botao enter para encerrar...')

