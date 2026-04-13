from rich import print
from rich.panel import Panel
from rich.console import Console
import os
import subprocess

console = Console()


class ControleRemoto:
    canal_min: int = 1
    canal_max: int = 10
    volume_min: int = 1
    volume_max: int = 10

    def __init__(self, canal=1, volume=2):
        self.canal_atual: int = canal
        self.volume_atual: int = volume
        self.ligado: bool = False

    def liga_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado and self.volume_atual < ControleRemoto.volume_max:
            self.volume_atual += 1

    def volume_menos(self):
        if self.ligado and self.volume_atual > ControleRemoto.volume_min:
            self.volume_atual -= 1

    def mostrar_tv(self):
        if not self.ligado:
            conteudo = "[bold red]:prohibited: A TV está desligada![/]"
        else:
            # Construção visual dos canais
            canais_str = ""
            for canal in range(self.canal_min, self.canal_max + 1):
                if canal == self.canal_atual:
                    canais_str += f"[black on yellow] {canal} [/] "
                else:
                    canais_str += f" {canal} "

            # Construção visual do volume
            vol_str = ""
            for v in range(self.volume_min, self.volume_max + 1):
                if v <= self.volume_atual:
                    vol_str += "[bold cyan]█[/]"
                else:
                    vol_str += "[white]░[/]"

            conteudo = f"CANAL: {canais_str}\n\nVOLUME: {vol_str}"

        tv_panel = Panel(conteudo, title="[bold blue][ TV ]", width=40, padding=(1, 2))
        console.print(tv_panel)


# Instância e Loop Principal
c = ControleRemoto()
while True:
    # Limpa a tela antes de mostrar a TV (funciona em Windows e Linux)
    subprocess.run(['cls' if os.name == 'nt' else 'clear'], shell=True)

    c.mostrar_tv()

    print(f"\n[bold]Comandos:[/] [p]Liga/Desliga [>]Canal+ [<]Canal- [+]Vol+ [-]Vol- [0]Sair")
    status = f"CH {c.canal_atual} | VOL {c.volume_atual}" if c.ligado else "OFF"
    comando = input(f"[{status}] >> ").lower().strip()

    match comando:
        case '0':
            break
        case 'p':
            c.liga_desliga()
        case '>':
            c.canal_mais()
        case '<':
            c.canal_menos()
        case '+':
            c.volume_mais()
        case '-':
            c.volume_menos()
#print("\n" *1)
print("[bold green]Sistema Finalizado!![/]")
