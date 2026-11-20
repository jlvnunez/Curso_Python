
class ContaBancaria:
    """
    Cria uma conta Bancaria e permite fazer saques e depositos
    """
    def __init__(self,id, nome, saldo =0):
        self.id =id #publico(+)
        self._titular = nome #protrgido(#)
        self.__saldo = saldo #privado (-)
        print(f'A conta {self.id} criada com sucesso! Saldo atual de R${self.__saldo:,.2F}')
        

    def __str__(self):
        #return f'A conta {self.id} de {self.titular} tem R${self.__saldo:,.2f} de saldo'
        return f"O estado atual da conta: {self.__dict__} "

    def depositar(self,valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Deposito de R$ {valor:,.2f} autorizado na conta {self.id}')

    def sacar(self,valor):
        valor =abs(valor)
        if valor > self.__saldo:
            print(f'Saque NEGADO de R$ {valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE')
        else:
            self.__saldo -= valor
            print(f'Saque de R$ {valor:,.2f} autorizado na conta {self.id}')
#print(c1.__doc__)
#c1 =ContaBancaria(112,"Gustavo",3000)
#c1.depositar(2500)
#c1.sacar(2_000_000)
#print(c1)






