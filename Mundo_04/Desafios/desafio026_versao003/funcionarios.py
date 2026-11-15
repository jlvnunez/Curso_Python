from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print

class Funcionario(ABC):
    salario_minimo = 1612
    desconto_inss = 7.5

    def __init__(self, nome=None): 
        self.nome = nome
        self.salario_bruto = 0
        self.salario = 0  

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        # Cria um painel formatado com os dados do funcionário
        desconto_valor = self.salario_bruto * self.desconto_inss / 100
        conteudo = (
            f"[bold cyan]Nome:[/bold cyan] {self.nome}\n"
            f"[bold green]Salário Bruto:[/bold green] R$ {self.salario_bruto:.2f}\n"
            f"[bold red]Desconto INSS ({self.desconto_inss}%):[/bold red] R$ {desconto_valor:.2f}\n"
            f"[bold yellow]Salário Líquido:[/bold yellow] R$ {self.salario:.2f}\n"
            f"Esse valor corresponde a {self.salario / self.salario_minimo:.2f} salários mínimos."
        )
        painel = Panel(conteudo, title=f"Relatório de {self.nome}", expand=False)
        print(painel)
             

class Funcionario_Horista(Funcionario):
    def __init__(self, nome, valor_hora=7.37, qtde_horas=220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = qtde_horas
        self.salario_bruto = self.valor_hora * self.horas_trabalhadas
    
    def calcular_salario(self):
        self.salario = self.salario_bruto - (self.salario_bruto * self.desconto_inss / 100)
        return self.salario

        
class Funcionario_Mensalista(Funcionario):
    def __init__(self, nome, salario_base=1612):
        super().__init__(nome)
        self.salario_bruto = salario_base
        
    def calcular_salario(self):
        self.salario = self.salario_bruto - (self.salario_bruto * self.desconto_inss / 100)
        return self.salario