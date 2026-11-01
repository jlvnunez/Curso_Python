from rich import print,inspect
class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self): 
        self.idade += 1 


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
   
    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer matricula") 


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
    
    def dar_aula(self):  
        print(f"{self.nome} comecou a dar aula")  


class Funcionario(Pessoa):
    def __init__(self, nome="", idade=0, cargo="", setor=""):
        super().__init__(nome, idade) 
        self.cargo = cargo
        self.setor = setor     

    def bater_Ponto(self):
        print(f"O Funcionario {self.nome} bateu o ponto")  


# Testando a criação de um aluno
a1 = Aluno("Jose Luis", 56, "Programacao", "T-01")
#print("Aluno:", a1.__dict__)
a1.fazer_aniversario()
a1.fazer_matricula()
inspect(a1,methods=True)




# Testando a criação de um professor
p1 = Professor("Ana Maria", 40, "Matemática", "Pleno")
#print("Professor:", p1.__dict__)
p1.fazer_aniversario()
p1.dar_aula()
inspect(p1,methods=True)

# Testando a criação de um funcionário
f1 = Funcionario("Carlos", 30, "Analista", "TI")
#print("Funcionário:", f1.__dict__)
f1.bater_Ponto()
f1.fazer_aniversario()
inspect(f1,methods=True)

#input("\nPressione [Enter] para sair...")