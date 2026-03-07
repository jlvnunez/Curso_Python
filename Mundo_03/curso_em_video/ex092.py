#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

print(f'{"Cadastro de Trabalhador":=^50}')
from datetime import datetime

dados={}
dados['nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de Nascimento: '))
dados['idade']= datetime.now().year -nasc
dados['ctps']= int(input('Carteira de Trabalho(0 Não tem) '))
if dados['ctps'] != 0:
        dados['Ano contratacao']=int(input('Ano de contratacao '))
        dados['Valor salario'] = float(input('Salario: R$  '))
        dados['Ano aposentadoria'] = dados['idade']+ (dados['Ano contratacao']+35)- datetime.now().year
else:
    print('\033[1;31mERRO!!DADOS INVALIDOS\033[m')
print('-'*30)    
for k , v in dados.items():
        print(f'{k} tem o Valor: {v}')
print()
