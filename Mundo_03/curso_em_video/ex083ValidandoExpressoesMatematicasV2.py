#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta
expr = str(input('Digite a expressão: '))
pilha = [] # Nossa "caixa de pratos"

for caractere in expr:
    if caractere == '(': 
        # Se abriu, "joga" na pilha
        pilha.append('(')
        
    elif caractere == ')':
        # Se fechou, precisamos ver se tem alguém para "fazer par"
        if len(pilha) > 0:
            pilha.pop() # Remove o último que abriu (casamento perfeito)
        else:
            # Se não tem ninguém na pilha e apareceu um ")", está errado!
            pilha.append(')') # Colocamos algo só para a pilha não ficar vazia
            break # Já sabemos que está errado, não precisa continuar lendo

# No final, checamos o tamanho da pilha
if len(pilha) == 0:
    print('Tudo certo! Expressão válida.')
else:
    print('Ops! A expressão está incorreta.')

    
