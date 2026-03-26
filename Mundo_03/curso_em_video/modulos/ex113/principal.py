#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

#programa principal
import funcoes
num1 = funcoes.leiaInt('Digite um valor Inteiro: ')
num2 = funcoes.leiaFloat('Digite um valor Real: ')
print(f'O valor digitado INTEIRO foi: {num1} e O valor REAL foi {num2}')