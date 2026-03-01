#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
print(f'{"DIVIDINDO VALORES EM LISTA":=^45}')
num = []
pares = []
impares = []
print('='*45)

while True:
     try:
         valor =int(input('Digite um valor: '))
         num.append(valor)
     except ValueError:   
         print('\033[31mVALOR INVÁLIDO! DIGITE APENAS NÚMEROS INTEIROS.\033[m')  
         continue
     resp =" "
     while resp not in'SN':
          resp =str(input('Quer Continuar? [S/N] ')).strip().upper()
          if resp == '':
                print('ERRO DIGITE APENAS S OU N')
          elif resp not in 'SN':
                print('\033[33mOpção inválida! Digite S para Sim ou N para Não.\033[m')
        
     if resp == 'N':
            break
     
for v in num:    
    if v %2==0:
         pares.append(v)
    elif v %2==1:
         impares.append(v)

print('=-'*45)
print(f'Lista COMPLETA {num}')
print(f'Lista PARES {pares}')
print(f'Lista IMPARES {impares}')


   
            

   
   
   
   
   
   
   