#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
# Inicialização das variáveis de controle
soma_idade = 0
maior_idade_homem = 0
nome_velho = ''
mulheres_novas = 0

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    
    # Soma das idades para a média
    soma_idade += idade
    
    # Lógica para o homem mais velho
    if sexo == 'M' and p == 1:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
        
    # Lógica para mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_novas += 1

media_idade = soma_idade / 4

print('\n' + '='*30)
print(f'A média de idade do grupo é de {media_idade:.1f} anos.')
if nome_velho == '':
    print('Não houve homens cadastrados.')
else:
    print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}.')
print(f'Ao todo são {mulheres_novas} mulheres com menos de 20 anos.')