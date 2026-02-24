#Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont=('zero','um','dois','tres','quatro',
      'cinco','seis','sete','oito','nove','dez',
      'onze','doze','treze','quatorze','quinze',
      'dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    try:
        num = int(input('Digite um numero entre 0 e 20 '))
        if 0<=num <=20:
           print(f'Voce digitou o numero {cont[num]}')
        
           resp=' '
           while resp not in 'SN':   
             resp = str(input('Quer continuar? [S/N] ')).strip().upper()  
           if resp == 'N':
             break
        else:
              print('Tente novamente! ',end='')
                
    except ValueError:
        print('Digite apenas numeros inteiros!!!')
print('{:=^30}'.format(' PROGRAMA ENCERRADO '))