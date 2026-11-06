from rich import print,inspect
from classes import Pessoa,Aluno,Professor,Funcionario

def main():
    # Testando a criação de um aluno
    a1 = Aluno("Jose Luis", 56, "Programacao", "T-01")
    #print("Aluno:", a1.__dict__)
    a1.fazer_aniversario()
    a1.fazer_matricula()
    #inspect(a1,methods=True)


    # Testando a criação de um professor
    p1 = Professor("Ana Maria", 40, "Matemática", "Pleno")
    #print("Professor:", p1.__dict__)
    p1.fazer_aniversario()
    p1.dar_aula()
    #inspect(p1,methods=True)

    # Testando a criação de um funcionário
    f1 = Funcionario("Carlos", 30, "Analista", "TI")
    #print("Funcionário:", f1.__dict__)
    f1.bater_Ponto()
    f1.fazer_aniversario()
    #inspect(f1,methods=True)
   
    a1.estudar()
    p1.estudar()
    f1.estudar()

if __name__=="__main__"  :
     main()     

     

#input("\nPressione [Enter] para sair...")