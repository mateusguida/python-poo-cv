from abc import ABC, abstractmethod

class poligono(ABC):
    def __init__(self, lados):
        self.qtd_lados = lados

    @abstractmethod
    def perimetro(self):
        pass
    
    @abstractmethod
    def area(self):
        pass