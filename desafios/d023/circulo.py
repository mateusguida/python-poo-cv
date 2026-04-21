from poligono import poligono
import math

class circulo(poligono):
    def __init__(self, raio):
        super().__init__(1)
        self.raio = raio

    def perimetro(self):
        return 2 * math.pi * self.raio
    
    def area(self):
        return math.pi * self.raio ** 2