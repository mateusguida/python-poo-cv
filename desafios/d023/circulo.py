from poligono import poligono
import math

class circulo(poligono):
    def __init__(self, raio = 1):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * math.pi * self.raio
    
    def area(self):
        return math.pi * self.raio ** 2