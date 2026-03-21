#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

#print('-='*25)
#print("     Interactive Helping System in Python   ")
#print('-='*25)

from time import sleep

# Tupla de cores otimizada para o VS Code
# 0: Reset | 1: Vermelho | 2: Verde | 3: Amarelo | 4: Azul | 5: Roxo | 6: Branco (Fundo)
c = (
    '\033[0m',         # 0 - Sem cores (Reset Absoluto)
    '\033[0;30;41m',   # 1 - Fundo Vermelho
    '\033[0;30;42m',   # 2 - Fundo Verde 
    '\033[0;30;43m',   # 3 - Fundo Amarelo
    '\033[0;30;44m',   # 4 - Fundo Azul
    '\033[0;30;45m',   # 5 - Fundo Roxo
    '\033[0;30;47m'    # 6 - Fundo Branco, Letra Preta (47 é mais estável que o 7)
)

def ajuda(com):
    """
    Exibe o manual do comando. O Python pausa a execução aqui
    até que você pressione 'q' para sair do manual.
    """
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    sleep(1)
    
    # Ativa a cor branca e limpa a linha para evitar vazamento
    print(c[6], end='', flush=True)
    
    # Chama o sistema de ajuda interativo
    help(com)
    print(c[0], end='', flush=True)
    input('\nPresione ENTER para voltar ao menu...')

    # RESET IMEDIATO: O \033[m reseta a cor e o \033[K limpa a linha atual
    print('\033[0m\033[K', end='', flush=True)
    sleep(1)

def titulo(msg, cor=0):
    """
    Cria um cabeçalho com moldura de '~' e cores.
    """
    tam = len(msg) + 4
    # Garante que não há cor anterior "sujando" o título
    print('\033[0m', end='') 
    
    print(c[cor], end='', flush=True)
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    
    # Fecha a cor e limpa a linha no VS Code
    print('\033[0m\033[K', end='', flush=True)
    sleep(1)

# --- PROGRAMA PRINCIPAL ---
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2) # Menu em Verde
    
    comando = str(input('Função ou Biblioteca (FIM para sair) > ')).strip()
    
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

# Mensagem de despedida
titulo('ATÉ LOGO!', 1) # Fim em Vermelho