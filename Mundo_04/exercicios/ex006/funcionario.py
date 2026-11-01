from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome="", idade=0, cargo="", setor=""):
        super().__init__(nome, idade) 
        self.cargo = cargo
        self.setor = setor     

    def bater_Ponto(self):
        print(f"O Funcionario {self.nome} bateu o ponto")  