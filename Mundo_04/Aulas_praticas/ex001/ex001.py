#declaracao da classe

class Gafanhoto:
    def __init__(self): #metodo construtor
        #atributos da instancia
        self.nome =""
        self.idade=0

    #metodos da instancia
    def aniversario(self):
        self.idade +=1


    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade"

#declaração de objetos
g1= Gafanhoto()
g1.nome = 'Maria'
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2= Gafanhoto()
g2.nome ="Jose Luis"
g2.idade = 54
g2.aniversario()
print(f'\033[1;32m{g2.mensagem()}\033[m')

g3= Gafanhoto()
g3.nome = "Claudia"
g3.idade= 53
print(f'\033[1;32m{g3.mensagem()}\033[m')
















