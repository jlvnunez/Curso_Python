#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str((input('Digite o sexo [M/F]: '))).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos>por favor digite seu sexo novamente![M/f]: ')).strip().upper()[0] #[0]se a pessoa digitar por exemplo masculino ele pega a primeira letra
print(f'Sexo {sexo} Registrado com Sucesso!')