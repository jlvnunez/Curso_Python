from rich import print
from rich.panel import Panel

class Churrasco:
    #atributos de classe
     consumo_padrao:float = 0.400 #media em de consumo por pessoa 400g
     preco_kg:float = 82.40

     def __init__(self,titulo,quant):
         #atributos de instancia
         self.titulo = titulo
         self.participantes = quant

     def __str__(self):
         return f'Esse e o {self.titulo} com {self.participantes} pessoas participando'
           
     def calcular_qtd_carne(self)->float:
         return self.participantes * Churrasco.consumo_padrao

     def calcular_custo_total(self)->float:
         return self.calcular_qtd_carne() *  self.__class__.preco_kg #ou Churrasco.preco_kg

     def calcular_custo_individual(self)->float:
         return self.calcular_custo_total() / self.participantes

     def analisar(self):
         conteudo=f"Analisando [green]{self.titulo}[/] com [blue]{self.participantes} convidados[/]"
         conteudo +=f"\nCada participante comerá {Churrasco.consumo_padrao} kg e cada kg custa R$ {Churrasco.preco_kg:,.2f}"
         conteudo += f"\nRecomendo comprar [blue]{self.calcular_qtd_carne():,.3f} kg[/] de carne"
         conteudo += f"\nO Custo total será de [green]{self.calcular_custo_total():,.2f}[/]"
         conteudo += f"\nCada pessoa pagará [yellow]R$ {self.calcular_custo_individual():,.2f}[/] para participar"
         painel = Panel(conteudo,title=self.titulo)
         print(painel)


c1= Churrasco("Churras dos amigos",quant=15)
c1.analisar()

c2 = Churrasco("Festa de fim de Ano",quant =150)
c2.analisar()



