# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# importante: as funções math.cos() e math.tan() esperam que o ângulo esteja em radianos, e não em graus. Por isso, precisamos converter o valor antes do cálculo.
import math
anguloGraus= float(input('Digite o angulo em graus '))

# Passo 1: Converter graus para radianos
anguloRad = math.radians(anguloGraus)
# Passo 2: Calcular Cosseno e Tangente
cosseno = math.cos(anguloRad)
tangente = math.tan(anguloRad)
print(f'O Cosseno de {anguloGraus}° é : {cosseno}\nA tangente de {anguloGraus}° é: {tangente}')