#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

catetoOposto = float(input("Digite o valor do primeiro cateto: "))
catetoAdjacente = float(input("Digite o valor do segundo cateto: "))

# A função hypot calcula a raiz quadrada da soma dos quadrados
hipotenusa = math.hypot(catetoOposto, catetoAdjacente)

print(f"A hipotenusa é: {hipotenusa:.2f}")