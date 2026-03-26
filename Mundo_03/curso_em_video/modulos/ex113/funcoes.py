def leiaInt(msg):
    while True:
        try:
           n=int(input(msg))
        except(ValueError,TypeError):
            print('\033[1;31m**Erro** Digite apenas numeros inteiros!\033[m')
            continue
        else:
            return n
        

def leiaFloat(msg):
    while True:
        try:
            n=float(input(msg))    
        except(ValueError,TypeError):
            print('**ERRO** Digite apenas Numeros reais')
            continue
        else:
            return n
