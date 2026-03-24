def leiadinheiro(msg):  #funcionar igual ao input
    valido = False
    while not valido:
        entrada=str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[1;31mErro!!"{entrada}" é preço invalido\033[m')
        else:
            valido = True
            return float(entrada)