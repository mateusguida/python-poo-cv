class Mae:
  def __init__(self, nome:str = "Mamãe"):
    self.nome = nome

  def fazer_pudim(self):
    print(f"{self.nome} está fazendo pudim.")

  def fritar_coxinha(self):
    print(f"{self.nome} está fritando coxinha.")

class Filho(Mae):
  def fritar_coxinha(self):
    print(f"{self.nome} está fritando coxinha de frango.")

class Filha(Mae):
  def fazer_pudim(self):
    print(f"{self.nome} está fazendo pudim de chocolate.")