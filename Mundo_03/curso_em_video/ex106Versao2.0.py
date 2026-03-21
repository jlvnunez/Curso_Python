#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

#print('-='*25)
#print("     Interactive Helping System in Python   ")
#print('-='*25)
from time import sleep

# Tupla de cores para o sistema
# 0: sem cores | 1: fundo vermelho | 2: fundo verde | 3: fundo azul | 4: fundo branco
c = (
    '\033[m',          # 0 - Reset
    '\033[0;30;41m',   # 1 - Vermelho
    '\033[0;30;42m',   # 2 - Verde
    '\033[0;30;44m',   # 3 - Azul
    '\033[7;30m'       # 4 - Branco (Inverso)
)

def ajuda(com):
    """
    Acessa o Interactive Help do Python com formatação visual.
    """
    titulo(f'Acessando o manual do comando \'{com}\'', 3)
    sleep(1)
    
    # Aplica a cor branca para o fundo do manual
    print(c[4], end='')
    help(com)
    
    # FORÇA O RESET IMEDIATO DA COR
    print(c[0], end='', flush=True)
    sleep(2)
    print('\n' * 2) # Pula linhas para limpar o visual

def titulo(msg, cor=0):
    """
    Cria um cabeçalho personalizado com moldura de '~' e cores.
    """
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='', flush=True) # Reset com flush para garantir a limpeza
    sleep(1)

# --- PROGRAMA PRINCIPAL ---
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2) # Título em Verde
    comando = str(input("Função ou Biblioteca (ou 'FIM' para sair) > ")).strip()
    
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

# Mensagem de encerramento em vermelho
titulo('ATÉ LOGO!', 1)
