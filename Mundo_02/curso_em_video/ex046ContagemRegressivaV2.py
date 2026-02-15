#Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
import emoji

print("CONTAGEM REGRESSIVA:")
for c in range(10, -1, -1):
    # O end='\r' faz o cursor voltar para o início da linha
    # O flush=True garante que o Python exiba o número imediatamente
    print(f"Lançamento em: {c} ", end='\r', flush=True)
    sleep(1)

print(emoji.emojize("\n\nBOOOOM! :fireworks: :sparkler:"))



