#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
print('-='*15)
print('     Funções Para Votação     ')
print('-='*15)
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <16:
        return f' Com {idade} anos:Não pode votar'
    elif 16 <= idade < 18 or idade >65:
        return f' Com {idade} anos: Voto Opcional'
    else:
        return f'Com {idade} anos: Voto Obrigatorio'
#programa principal
nasc= int(input('Ano de Nascimento: '))
print(voto(nasc))
print('-='*15)

input('clique enter para encerrar')

 