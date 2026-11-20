from ex008 import ContaBancaria

def main():
    c1 =ContaBancaria(111,"Jose",5_000)
    c1.depositar(1_000)
    
    #c1._titular ="Pedro" #ele deixa,pois nao mexer - adultos consentindo
    #c1.sacar(100)
    c1.__saldo=0
    #c1._ContaBancaria__saldo=0 #ele deixa mexer adultos consentindo
    print(c1)






if __name__== "__main__":
    main()