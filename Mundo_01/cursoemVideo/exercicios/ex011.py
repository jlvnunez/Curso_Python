#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
# Lendo os dados de entrada

largura = float(input('Largura da parede (em metros): '))
altura = float(input('Altura da parede (em metros): '))

# Calculando a área
area = largura * altura

# Calculando a quantidade de tinta
# Como 1L pinta 2m², dividimos a área total por 2
tinta = area / 2

print("-" * 40)
print(f'Sua parede tem a dimensão de {largura} x {altura} e sua área é de {area:.2f}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}L de tinta.')
print("-" * 40)