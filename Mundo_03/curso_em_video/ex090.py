#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

print(f'{"Dicionario em Python":=^50}')


boletim = {}
boletim['nome'] = str(input('Nome '))
boletim['media']= float(input(f'Media de {boletim["nome"]}: '))
if boletim['media']>=7:
    boletim['situacao']='Aprovado'
elif 5 <= boletim['media'] <7:
    boletim['situacao']='Recuperacao'
else:
    boletim['situacao']= 'Reprovado'
print('-='*30)
for k, v in boletim.items():
    print(f'— {k} igual a {v}')

print('-='*30)

input('aperte para finalizar...')

