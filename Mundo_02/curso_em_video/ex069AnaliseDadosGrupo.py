#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
print('Analise de Dados no grupo'.center(50,'-'))
tot18 = homem = mulher20 =0
while True:
    idade=int(input('Idade '))
    sexo = ' '
    while sexo not in 'MF':
         sexo =str(input('Sexo [M/F] ')).strip().upper()[0]
         if idade >=18:
            tot18+=1
         if sexo == 'M':
            homem+= 1    
         if sexo == 'F' and idade < 20:
            mulher20 += 1

    resp =' '
    while resp not in 'SN':  
        resp =input('Quer continuar?[S/N] ').strip().upper()[0]
    if resp =='N':
         break
print('='*50)    
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de Homens cadastrados: {homem}')
print(f'Total de Mulheres com menos de 20 anos: {mulher20}')

     

    