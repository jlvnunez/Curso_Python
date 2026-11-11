from abc import ABC,abstractmethod

class Transporte(ABC):
    def __init__(self,distancia):
        self.distancia= distancia
        self.frete=0

    @abstractmethod
    def calcular_Frete(self):
        pass


class Moto(Transporte):
    fator = 0.50
    def __init__(self,distancia):
        super().__init__(distancia)
    
    def calcular_Frete(self):
        self.frete = self.distancia * Moto.fator
        return f"R${self.frete:.2f}"


class Caminhao(Transporte):
    fator=1.20
    def __init__(self,distancia):
        super().__init__(distancia)
    
    def calcular_Frete(self):
        if self.distancia <50:
            self.frete= 0
            return"Raio Mínimo de 50km"
        else:
            self.frete = self.distancia *Caminhao.fator
            return f"R${self.frete:.2f}"


class Drone(Transporte):
    fator=9.50  
    def __init__(self,distancia):
            super().__init__(distancia)
    
    def calcular_Frete(self): 
        if self.distancia > 10:
            self.frete=0
            return"Raio Maximo 10km"
        else:
            self.frete=self.distancia *Drone.fator
            return f"R${self.frete:.2f}"
       
       
       
        
