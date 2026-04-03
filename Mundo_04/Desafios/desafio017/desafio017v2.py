from rich import print
from rich.panel import Panel


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = float(preco)

    def __str__(self):
        return f"{self.nome} custa R$ {self.preco:,.2f}"

    def etiqueta(self):
        # Formatando o preço com padrão brasileiro (usando substituição simples)
        preco_br = f"{self.preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        # Criando o conteúdo com alinhamento
        # \n pula linha, e definimos uma largura fixa para o center
        largura_interna = 30
        conteudo = f"{self.nome.upper().center(largura_interna)}\n"
        conteudo += f"{'-' * largura_interna}\n"
        conteudo += f"VALOR: R$ {preco_br.center(largura_interna - 10)}"

        # Gerando o painel
        etiqueta = Panel(conteudo, title="[bold blue]Cupom[/]", width=34, padding=(1, 1))
        print(etiqueta)


# Testando os objetos
p1 = Produto("Iphone 17 Pro Max", 17000.00)
p1.etiqueta()

p2 = Produto("Notebook", 5000.00)
p2.etiqueta()