#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('=' *36)
print('Super P.A usando while')
print('=' *36)

primeiro = int(input('Valor primeiro termo: '))
razao =int(input("Razao "))
termo = primeiro
c=1
total = 0
mais =10
while mais != 0:
    total = total + mais
    while c  <= total:
        print(f'{termo}-> ',end='')
        termo +=razao
        c+=1       
    print('Pausa...')
    
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print(f'progressao finalizada com {total} termos')
print('FIM !!!')    