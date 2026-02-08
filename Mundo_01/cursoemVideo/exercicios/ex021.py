#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
#import pygame nao funciona 
import os
# 1. Pega o caminho completo de onde o seu script ex021.py está salvo
caminho_da_pasta = os.path.dirname(r"C:\Users\jlvnunez\Documents\cursoPython")

# 2. Junta o caminho da pasta com o nome do arquivo de música
caminho_completo = os.path.join(r"C:\Users\jlvnunez\Documents\cursoPython\projetos-cursoemVideo\exercicios\chicago.mp3")

# 3. Verifica e tenta abrir
if os.path.exists(caminho_completo):
    print(f"Sucesso! Abrindo: {caminho_completo}")
    os.startfile(caminho_completo)
else:
    print("ERRO: O arquivo 'chicago.mp3' não está na mesma pasta que este script!")
    print(f"Pasta atual onde procurei: {caminho_da_pasta}")