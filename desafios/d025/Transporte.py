from abc import ABC, abstractmethod

class Transporte(ABC):
    
    def __init__(self, distancia, frete):
        self.distancia = distancia
        self.frete = frete

    @abstractmethod
    def calc_frete(self):
        pass
    
# Classe Moto
class Moto(Transporte):
    
    def __init__(self, distancia, frete):
        super().__init__(distancia, frete)
        self.fator = 0.50

    def calc_frete(self):
        return (f"R$ [green]{self.distancia * self.fator}")
    
# Classe Caminhão
class Caminhao(Transporte):
    
    def __init__(self, distancia, frete):
        super().__init__(distancia, frete)
        self.fator = 1.20

    def calc_frete(self):
        if self.distancia >= 50:
            return (f"R$ [green]{self.distancia * self.fator}")
        else:
            return(f"Raio mínimo de 50 km.")
    
# Classe Drone
class Drone(Transporte):
    def __init__(self, distancia, frete):
        super().__init__(distancia, frete)
        self.fator = 9.50

    def calc_frete(self):
        if self.distancia <= 10:
          return (f"R$ [green]{self.distancia * self.fator}")
        else:
          return(f"Raio máximo de 10 km.")