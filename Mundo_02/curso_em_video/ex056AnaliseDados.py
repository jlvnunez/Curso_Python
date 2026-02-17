#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho =''
totMulher20 = 0
for p in range(1,5):
    print(f'------{p}ª PESSOA------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in'Mm':
       maiorIdadeHomem = idade
       nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem =idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1

mediaIdade = somaIdade /4    
print(f'A media da idade do grupo e {mediaIdade} anos')
print(f'O Homem mais velho tem {maiorIdadeHomem} e se chama {nomeVelho}')
print(f'Ao todo são {totMulher20} Mulheres com menos de 20 anos')
