#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
print('-=-'*20)
distancia = float(input('Distancia à percorrer em KM '))
if distancia <= 200:
    precoKm = 0.50
else:
    precoKm = 0.45

resultado = distancia * precoKm
print(f' \033[32mO preço da passagem será:R$ {resultado:.2f} reais\033[m')

       
    