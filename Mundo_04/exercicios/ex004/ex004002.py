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
        pass 


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
    
    def dar_aula(self):  
        pass  


class Funcionario(Pessoa):
    def __init__(self, nome="", idade=0, cargo="", setor=""):
        super().__init__(nome, idade) 
        self.cargo = cargo
        self.setor = setor     


# Testando a criação de um aluno
a1 = Aluno("Jose Luis", 56, "Programacao", "T-01")
print("Aluno:", a1.__dict__)

# Testando a criação de um professor
p1 = Professor("Ana Maria", 40, "Matemática", "Pleno")
print("Professor:", p1.__dict__)

# Testando a criação de um funcionário
f1 = Funcionario("Carlos", 30, "Analista", "TI")
print("Funcionário:", f1.__dict__)

input("\nPressione [Enter] para sair...")