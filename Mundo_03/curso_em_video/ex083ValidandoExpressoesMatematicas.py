#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
print('='*40)
print(f'{"Validando Expressoes Matematicas":=^40}')
expr= str(input('Digite a expressao '))
pilha=[]
for simbolo in expr:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha)> 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:

    print('\033[1;32mEXPRESÃO VALIDA!!\033[m')
else:
    print('\033[1;31mEXPRESÃO INVALIDA!!\033[m')
print('='*40)


    
    
