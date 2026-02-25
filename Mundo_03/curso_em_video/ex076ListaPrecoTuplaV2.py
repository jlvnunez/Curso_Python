#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# A tupla única com dados intercalados (Produto, Preço)
listagem = ('Lápis', 1.75, 
            'Borracha', 2.00, 
            'Estojo', 15.90, 
            'Transferidor', 4.20, 
            'Compasso', 9.99, 
            'Mochila', 120.32, 
            'Canetas', 22.30, 
            'Livros', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

# O segredo está aqui:
# listagem[0::2] pega todos os itens começando do 0, pulando de 2 em 2 (Nomes)
# listagem[1::2] pega todos os itens começando do 1, pulando de 2 em 2 (Preços)
for produto, preco in zip(listagem[0::2], listagem[1::2]):
    print(f'{produto:.<30}R${preco:>8.2f}')

print('-' * 40)



