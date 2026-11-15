from rich import inspect
from funcionarios import *

def main():
    f1=Funcionario_Horista("Jose Luis", 45, 220)
    f1.calcular_salario()
    f1.analisar_salario()
    #inspect(f1)

    f1 =Funcionario_Mensalista("Claudia", salario_base= 5000)
    f1.calcular_salario()
    f1.analisar_salario()


if __name__ == "__main__":
    main()

print("=" * 70)    