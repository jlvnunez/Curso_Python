#Exercício Python 115a: Vamos criar um menu em Python, usando modularização.
#Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.
#Exercício Python 115c: Vamos finalizar o projeto de acesso a arquivos em Python.


#programa principal
from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if resposta ==1:
        lerArquivo(arq)
    elif resposta ==2:
        cabecalho('NOVO CADASTRO')
        nome=str(input('Nome: '))
        idade=leiaInt('Idade: ')
        cadastrar(arq,nome,idade)     
    elif resposta == 3:
        cabecalho('SAINDO DO SISTEMA... ATÉ LOGO!!!')
        break
    else:
        print('\033[1;31mErro! Digite uma opcao Valida!\033[m')
    sleep(2)





