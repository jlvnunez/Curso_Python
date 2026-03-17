#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 

print()
def escreva(msg):
    tam=len(msg)
    print('='*tam)
    print(msg)
    print('='*tam)

#programa principal
escreva("Um Print Especial exercicio 97")
escreva("Gustavo Guanabara")    
escreva("Curso de Python")
escreva("Curso em Video") 