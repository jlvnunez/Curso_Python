#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

print('-='*35)
print("     Validando entrada de dados em Python com Função   ")
print('-='*35)
def leiaInt(frase):
    while True:
        dado = input(frase)
        if dado.isnumeric():
            return int(dado)
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')

# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número\033[1;32m {n}\033[m')

