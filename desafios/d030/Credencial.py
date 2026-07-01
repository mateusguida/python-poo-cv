class Credencial:
  def __init__(self):
    self.senha = "123456"
    self.__hash = self.validar(self.senha)
  
  def validar(self, senha):
    pass