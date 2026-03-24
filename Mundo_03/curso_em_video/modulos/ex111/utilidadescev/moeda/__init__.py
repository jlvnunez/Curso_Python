def aumentar(preco=0,taxa=0,format=False):
    res = preco + (preco *taxa /100)
    return res if not format else moeda(res)

def diminuir(preco=0,taxa=0,format=False):
    res = preco - (preco *taxa /100)
    return res if not format else moeda(res)

def dobro(preco=0,format=False):
    res = preco *2
    return res if not format else moeda(res)

def metade(preco=0,format=False):    
    res= preco/2
    return res if not format else moeda(res)

def moeda(preco=0,moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.',',')

def resumo(preco=0,taxaA=30,taxaD=25):
    print('='*30)
    print('Resumo do Valor'.center(30))
    print('='*30)
    print(f'Preco Analisado:\t{moeda(preco)}')   #\t = tabulacao
    print(f'O dobro do preço:\t{dobro(preco,True)}')
    print(f'Metade do preço:\t{metade(preco,True)}')
    print(f'{taxaA}% de aumento:\t\t{aumentar(preco,taxaA,True)}')
    print(f'{taxaD}% desconto:\t\t{diminuir(preco,taxaD,True)}')
    print('='*30)