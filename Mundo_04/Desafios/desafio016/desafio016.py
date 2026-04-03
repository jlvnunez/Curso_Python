from rich import print
from rich import inspect

class Funcionario:
       #Atributos de Classe
    empresa = "Curso em Video"

    def __init__(self,nome,setor,cargo):
        #atributos de instancia
        self.nome =nome
        self.setor =setor
        self.cargo =cargo

    def apresentacao(self)->str:
        return f':handshake:Ola,sou [blue]{self.nome}[/],eu sou {self.cargo} do setor de {self.setor} da empresa [blue]{Funcionario.empresa}[/]'


c1= Funcionario("Maria","Administração","Diretora")
print(c1.apresentacao())
#inspect(c1)
#inspect(c1,methods=True)

Funcionario.empresa= "Falcao"
c2= Funcionario("Pedro","TI","Programador")
print(c2.apresentacao())
#inspect(c2)
#inspect(c2,methods=True)

c3= Funcionario("Pedro","TI","Programador")
print(c3.apresentacao())
#inspect(c3)
#inspect(c3,methods=True)

#inspect(Funcionario)








