from rich import print
from rich import inspect

#print(int.__dict__)
#inspect(int,all=True)
class ContaBancaria:
    """
    Cria uma conta Bancaria e permite fazer saques e depositos
    """
    def __init__(self,id, nome, saldo =0):
        self.id =id
        self.titular = nome
        self.saldo = saldo
        print(f'A conta {self.id} criada com sucesso.Saldo atual de {self.saldo:,.2F}')

    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo'

    def depositar(self,valor):
        self.saldo += valor
        print(f'Deposito de R$ {valor:,.2f} autorizado na conta {self.id}')

    def sacar(self,valor):
        if valor > self.saldo:
            print(f'Saque NEGADO de R$ {valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE')
        else:
            self.saldo -= valor
            print(f'Saque de R$ {valor:,.2f} autorizado na conta {self.id}')
#print(c1.__doc__)
c1 =ContaBancaria(112,"Gustavo",3000)
c1.depositar(500)
c1.sacar(2_000_000)

#print(c1)
c=ContaBancaria(id="111",nome="Jose",saldo=500)
inspect(c)