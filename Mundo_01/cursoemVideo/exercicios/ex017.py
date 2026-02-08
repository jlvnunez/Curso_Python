#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

catetoOposto= float(input('Digite o comprimento cateto oposto '))
catetoAdjacente = float(input('Digite comprimento cateto adjacente '))
hipotenusa= (catetoOposto **2 + catetoAdjacente **2)** 0.5

print(f'comprimento cateto oposto:  {catetoOposto}\nComprimento cateto adjacente = {catetoAdjacente}\n Hipotenusa = {hipotenusa}')
     
     

