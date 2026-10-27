class Pessoa:
    def __init__(self,nome="",idade=0):
        self.nome = nome
        self.idade= idade

    def fazer_aniversario(self): 
        self.idade +=1 


class Aluno(Pessoa):
    def __init__(self,nome,idade,curso,turma):
        super().__init__(nome, idade)
        self.curso=curso
        self.turma=turma
   
    def fazer_matricula(self):
        pass 
   

class Professor(Pessoa):
    def __init__(self,nome,idade,especialidade,nivel):
        super().__init__(nome,idade),
        self.especialidade= especialidade
        self.nivel= nivel
    
    def dar_aula(self):  
       pass  

class Funcionario(Pessoa):
    def __init__(self, nome, idade,cargo,setor):
        super().__init__(nome,idade) 
        self.cargo=cargo
        self.setor=setor      


a1=Aluno("Jose Luis",56,"Programacao","T-01")
print("Aluno:",a1.__dict__)

p1=Professor("Carlos",55,"matematica","superior")
print("Professor:",p1.__dict__)

f1=Funcionario("Maria",35,"gerente","setor")
print("Funcionario:",f1.__dict__)