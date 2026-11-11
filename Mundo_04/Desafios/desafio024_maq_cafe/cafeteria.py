from abc import ABC, abstractmethod
class BebidaQuente(ABC):
    def preparar(self):
        print("---Iniciando o Preparo---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("---Bebida Pronta---\n")


    def ferver_agua(self):
        print("1. Fervendo a agua à 100 graus Celsius.")

    @abstractmethod   
    def misturar(self):
        pass
    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
     def misturar(self):
         print("2.Passando agua pressurizada pelo pó do cafe moido")
         #return super().misturar()
         
     def servir(self):
         print("3. Servir em Xicara pequena")
         #return super().servir()
         
         
class Cha(BebidaQuente):
    def misturar(self):
        print("2 Mergulhando o sache de ervas na agua")
        #return super().misturar()
    
    def servir(self):
        print("Servindo na caneca de porcelana com limão")
        #return super().servir()


class Leite(BebidaQuente):
    def misturar(self):
        print("2.Passando vapor presurizada pelo bico do leite")
        #return super().misturar()
    
    def servir(self):
        print("3. Servindo na caneca grande com cafe")
        #return super().servir()    