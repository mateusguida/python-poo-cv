from poligono import poligono

class quadrado(poligono):
  def __init__(self, lados):
    super().__init__(lados)
  
  def perimetro(self):
    return self.qtd_lados * 4
  
  def area(self):
    return self.qtd_lados ** 2