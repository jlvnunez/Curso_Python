#xercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print('=' * 20)
try:
    # Tudo o que está recuado aqui embaixo pertence ao 'try'
    numero = int(input('Digite Um Numero inteiro: '))
    print('''
        Opcao [1]Converter para BINARIO
        Opcao [2]Converter para OCTAL
        Opcao [3]Converter para HEXADECIMAL ''') 
    
    opcao = input('Escolha a opção acima: ')

    # O 'if' fica aqui dentro porque ele depende do 'numero' ter dado certo
    if opcao == '1':
        print(f'\033[32mO Numero {numero} convertido em Binario é {bin(numero)[2:]}\033[m')
    elif opcao == '2':
        print(f'\033[32mO Numero {numero} convertido em Octal é {oct(numero)[2:]}\033[m')
    elif opcao == '3':
        print(f'\033[32mO Numero {numero} convertido em Hexadecimal é : {hex(numero)[2:].upper()}\033[m')
    else:
        print('\033[31mOpção Invalida! tente novamente.\033[m')

except ValueError:
    # Este print precisa estar recuado para pertencer ao except
    print('\033[31mErro: Você precisa digitar um número inteiro válido!\033[m')

input('Aperte ENTER para fechar...') # <--- ESSA LINHA É OBRIGATÓRIA
