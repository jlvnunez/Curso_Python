#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('=' *36)
print('progressao Aritimetica usando while')
print('=' *36)

primeiro = int(input('Valor primeiro termo: '))
razao =int(input("Razao "))
termo = primeiro
c=1

while c  <= 10:
       print(f'{termo}-> ',end='')
       termo +=razao
       c+=1       

print('FIM')
     

