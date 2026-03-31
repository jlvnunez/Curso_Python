#declaracao da classe
class Gafanhoto:
    """
    -Essa Classe cria um Gafanhoto,que é uma pessoa que tem nome e idade
    -Para Criar uma nova pessoa use
    Variavel = Gafanhoto(nome,idade)
    """
    def __init__(self,nome="Desconhecido",idade=0): #metodo construtor
        #atributos da instancia
        self.nome = nome
        self.idade=idade

    #metodos da instancia
    def aniversario(self):
        self.idade +=1

    def __str__(self): #Dunder Method
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f'Estado: nome= {self.nome} ; idade = {self.idade}'
#declaração de objetos
g1= Gafanhoto("maria",17)
g1.aniversario()

#print(g1)
#print(g1.__dict__) #Attribute sem parenteses
print(g1.__getstate__()) #Method tem parenteses
print(g1.__class__)
print(g1.__doc__) #Dunder Attribute

















