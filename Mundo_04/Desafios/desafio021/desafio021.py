from rich import print
class Caneta:
    def __init__(self,cor="azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha="[blue]"
            case "vermelha"| "vermelho":
                escolha="[red]"
            case "verde":
                escolha ="[green]"
            case _:
                escolha = "[white]"
        self.cor=escolha
        self.tampada =True


    def escrever(self,msg):
        if self.tampada:
            print(f":prohibited:A {self.cor} caneta esta tampada")
        else:
            print(f"{self.cor}{msg}[/]",end=" ")

    """Transformar em @staticmethod (Recomendado)
Você adiciona um "decorador" acima da função e remove o self. Isso avisa ao Python (e ao editor) que este método é uma utilidade da classe, mas não precisa de dados da instância para rodar."""
    @staticmethod
    def quebrar_linha(qtd = 1):
        """Pula um número determinado de linhas no terminal."""
        print("\n" * qtd,end='')


    def tampar(self):
        self.tampada=True


    def destampar(self):
        self.tampada =False

    def __repr__(self):
        status = "tampada" if self.tampada else "destampada"
        return f"Caneta(cor={self.cor}, status={status})"

c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")
c4 = Caneta("")
c1.destampar()
c2.destampar()
c3.destampar()
c4.destampar()

c1.escrever("Ola Mundo!")
print(c1)
c2.escrever("Funciona!")
print(c2)
c2.quebrar_linha(2)
c3.escrever("Deu Certo!")
print(c3)
c4.escrever("Ola Mundo!")
c4.tampar()
print(c4)
c3.quebrar_linha(2)
#c1.tampar()
c1.escrever("Será que rola?")
print(c1)

#print(c1)
#print(c2)
#print(c3)


