#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
print('-='*20)
print("     Validando entrada de dados em Python com Função   ")
print('-='*20)

def leiaInt(msg):
    ok=False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('Erro! Digite um numero inteiro valido!')
        if ok:
            break
    return valor



#programa principal

n=leiaInt('Digite um Numero: ')    
print(f'Voce acabou de digitar o numero {n}')