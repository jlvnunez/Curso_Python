
from lib.interface import *
import os

def arquivoExiste(nome):
    try: 
        a=open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a=open(nome,'wt+')
        a.close()    
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a=open(nome,'rt')
    except:
        print('ERRO ao ler arquivo')   
    else:
        cabecalho('Pessoas Cadastradas')
        
        for linha in a:
           dado = linha.split(';')
           if len(dado) == 2: # Só tenta imprimir se houver Nome e Idade
             nome = dado[0].strip()
             idade = dado[1].replace('\n', '').strip()
             print(f'{nome:<30}{idade:>3} anos')
    finally:
            a.close()


def cadastrar(arq,nome='desconhecido',idade=0):
    try:
        a= open(arq,'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n ')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()







    
       
