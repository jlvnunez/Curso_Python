from personagem_rpg import *
from rich import inspect

def main():
    p1 =Guerreiro("Pikachu",1000)
    #p1.receber_dano(100)
    p2 = Mago("Gandalf",2000)
    #inspect(p1,methods=True)

    p1.atacar(p2,200)
    p2.atacar(p1,200)
    p1.curar()
    p2.curar()


if __name__ == "__main__":
     main()

   