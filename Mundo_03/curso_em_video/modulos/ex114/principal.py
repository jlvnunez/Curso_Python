#Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.request
import urllib.error

# Definimos um "User-Agent" (identidade de um navegador real)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

try:
    # Criamos uma requisição fingindo ser um navegador
    req = urllib.request.Request('https://www.cursoemvideo.com', headers=headers)
    site = urllib.request.urlopen(req)
except urllib.error.HTTPError as erro:
    print(f'Erro de HTTP: {erro.code}') # Aqui ele mostraria o 403
except urllib.error.URLError as erro:
    print(f'Erro de rede: {erro.reason}')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
    # Agora você pode até ler o conteúdo se quiser:
    # print(site.read().decode('utf-8'))