# --- Exemplo de teste ---
from funcionarios import *

if __name__ == "__main__":
    horista = Funcionario_Horista("Carlos", valor_hora=15.0, qtde_horas=160)
    horista.calcular_salario()
    print(f"Horista {horista.nome} - Salário líquido: R$ {horista.salario:.2f}")

    mensalista = Funcionario_Mensalista("Ana", salario_base=3000.0)
    mensalista.calcular_salario()
    print(f"Mensalista {mensalista.nome} - Salário líquido: R$ {mensalista.salario:.2f}")