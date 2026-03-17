#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

print(f'{"Unindo Dicionarios e Listas":=^50}')

pessoa={}
galera= list()
soma=media=0
while True:    
    pessoa.clear()
    pessoa['nome']= str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo [M/F]: ")).upper()[0]
        if pessoa['sexo'] in "MF":
            break
        print("ERRO!Digite apenas M ou F")
    
    pessoa['idade']=int(input("idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input("Quer continuar? [S/N]: ")).upper()[0]
        if resp in "SN":
            break
        print("ERRO!! digite apenas [S ou N]")
    if resp == "N":
        break   
print('-'*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A media da idade e de {media:5.2f} anos')
print('C) As Mulheres cadastradas foram ',end='')
for p in galera:
    if p['sexo'] in "Ff":
        print(F'{p['nome']} ',end='')
print()
print('D) Listas das pessoas acima da media:\n',end='')
for p in galera:
    if p['idade'] >= media:
        print('',end='')
        for k,v in p.items():
            print(f'{k} = {v} ',end='')
        print()    
print('Encerrado!!!')        



