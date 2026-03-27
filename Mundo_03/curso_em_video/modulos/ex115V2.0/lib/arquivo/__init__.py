
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
        a = open(nome, 'rt', encoding='utf-8')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        dados_para_exibir = []
        
        for linha in a:
            dado = linha.split(';')
            if len(dado) == 2:
                # .strip() remove espaços extras no início e no fim
                nome_limpo = dado[0].strip() 
                idade_limpa = dado[1].strip().replace('\n', '')
                dados_para_exibir.append([nome_limpo, idade_limpa])
        
        # Agora a ordem alfabética funcionará perfeitamente
        dados_para_exibir.sort(key=lambda x: x[0].lower())
        
        for pessoa in dados_para_exibir:
            # O :<30 garante que todos comecem na mesma coluna
            print(f'{pessoa[0]:<30}{pessoa[1]:>3} anos')
            
    finally:
        a.close()



def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        # Importante: o 'encoding' garante que nomes com acento não quebrem o texto
        a = open(arq, 'at', encoding='utf-8')
    except:
        print('\033[31mERRO NA ABERTURA DO ARQUIVO!\033[m')
    else:
        try:
            # Removendo aquele espaço extra que causava o erro de alinhamento
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mERRO AO GRAVAR OS DADOS!\033[m')
        else:
            print(f'\033[32mNOVO REGISTRO DE {nome} ADICIONADO COM SUCESSO!!.\033[m')
            a.close()


def removerRegistro(arq, nome_deletar):
    try:
        with open(arq, 'rt') as f:
            linhas = f.readlines()
        
        with open(arq, 'wt') as f:
            encontrado = False
            for linha in linhas:
                # Divide a linha para comparar apenas o nome (antes do ';')
                dados = linha.split(';')
                if dados[0].strip().lower() != nome_deletar.strip().lower():
                    f.write(linha)
                else:
                    encontrado = True
            
            if encontrado:
                print(f'\033[32mRegistro de {nome_deletar} removido!\033[m')
            else:
                print(f'\033[31mNome "{nome_deletar}" não encontrado.\033[m')
    except Exception as e:
        print(f'Erro ao processar arquivo: {e}')




    
       
