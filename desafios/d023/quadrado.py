from poligono import poligono

class quadrado(poligono):
  def __init__(self, lado = 1):
    super().__init__(4)
    self.lado = lado
  
  def perimetro(self):
    return self.lado * 4
  
  def area(self):
    return self.lado ** 2