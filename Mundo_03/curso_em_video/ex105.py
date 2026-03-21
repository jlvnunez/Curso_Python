#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
print('-='*25)
print("     Analisando e gerando Dicionarios usando função   ")
print('-='*25)
def notas(*n,sit=False):
    """
    -> Função Para analisar notas e situações de varios alunos
    :Param n:Uma ou mais notas dos alunos(aceita varios alunos)
    :Param sit:Valor Opcional (aceita ou nao a situação)
    :return:Dicionario com varias informações sobre situação da turma
    """
    
    d={}
    print(n)
    d['total']=len(n)
    d['maior']=max(n)
    d['menor']=min(n)
    d['media']=sum(n)/len(n)
    if sit:
        if d['media']>=7:
            d['situacao']='BOA'
        elif d['media'] >=5:
            d['situacao']='RAZOAVEL'
        else:
            d['situacao']= 'RUIM'
    return d
      
#programa principal
dados=notas(3.5,2.5,2.5,7,8,sit=True)
print(dados)
help(notas)
