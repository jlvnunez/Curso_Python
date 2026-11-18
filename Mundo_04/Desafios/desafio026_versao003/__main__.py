from funcionarios import *
from rich import print


if __name__ == "__main__":
    horista = Funcionario_Horista("Joao", valor_hora=30.0, qtde_horas=220)
    horista.calcular_salario()
    horista.analisar_salario()
    print(f"Horista {horista.nome} - Salário líquido: [green]R$ {horista.salario:.2f}[/] referente à [green]({horista.horas_trabalhadas})[/]horas trabalhadas.\n")

    mensalista = Funcionario_Mensalista("Maria", salario_base=10000.0)
    mensalista.calcular_salario()
    mensalista.analisar_salario()
    print(f"Mensalista {mensalista.nome} - Salário líquido: R$ {mensalista.salario:.2f}")