#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#–#Quantas letras tem o primeiro nome.

nome = str(input('Digite seu Nome Completo '))
print('Analisando seu Nome...')
print(f'Seu nome em letras Maiusculas é {nome.upper()}')
print(f'Seu nome em letras minusculas é {nome.lower()}')

''' nome.split(): Transformou o nome em uma lista: ['Jose', 'Luis', 'Valtuille', 'Nunez'].

"".join(...): Juntou as palavras da lista usando "nada" como separador, resultando em: "JoseLuisValtuilleNunez".

Faltou o len(): Sem o len, o f-string entende que você quer exibir o texto resultante, e não contar os caracteres dele.'''
print(f'Seu Nome tem ao todo {len("".join(nome.split()))}')

print(f'O primeiro Nome é {nome.split()[0]} e ele tem {nome.find(' ')} letras.')