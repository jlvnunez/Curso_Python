from transportes import *
from rich import print,inspect
from rich.table import Table
print()
def main():
    dist=20
    """entrega = Moto(dist)
    print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calcular_Frete()}\n")"""

    dist=80
    """entrega = Caminhao(dist)
    print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calcular_Frete()}\n")""" 


    dist=25
    viagem =[Moto(dist),Caminhao(dist),Drone(dist)] 
    #inspect(viagem)
    """entrega = Drone(dist)
    print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calcular_Frete()}\n") """

    tabela=Table(title="Tabela de fretes")
    tabela.add_column("Distancia")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")

    for item in viagem:
        tabela.add_row(f"{dist} KM",f"{type(item).__name__}",f"{item.calcular_Frete()}")
    print(tabela)


if __name__ == "__main__":
    main()   