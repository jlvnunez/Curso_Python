# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

'''Operação Original	Forma Simplificada
            n = n + 1	n += 1
            n = n - 1	n -= 1
            n = n * 2	n *= 2
            n = n / 2	n /= 2
      n = n ** 2 (Potência)	n **= 2'''
      # raiz = n ** 0.5 0u 1/2

n= int(input('Digite um Numero  '))
antecessor = n -1
sucessor= n +1
print('O numero antecessor é {}\n O numero sucessor é {}'.format(antecessor,sucessor) )
