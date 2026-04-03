from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = float(preco)

    def __str__(self):
        return f"{self.nome} custa R$ {self.preco:,.2f}"


    def etiqueta(self):
        conteudo = f"{self.nome.center(30,' ')}"
        conteudo += f"{'-' *30}"
        precof = f"{self.preco:,.2f}"
        conteudo += f"R${precof.center(26,' ')}"
        etiqueta = Panel(conteudo,title="Produto",width=34)
        print(etiqueta)

p1= Produto("Iphone 17 Pro Max", "17_000.00")
p2= Produto("Notebook Gamer","5_000.00")
p1.etiqueta()
p2.etiqueta()
#print(p1)
#print(p2)
