class Avaliacao:
  def __init__(self, nome, disciplina, nota = 0.0):
    self.nome = nome
    self.disciplina = disciplina
    self._nota = nota

  # Criando atributo validável
  @property
  def nota(self): # getter
    return self._nota
  
  @nota.setter
  def nota(self, valor): # setter
    if 0 <= valor <= 10:
      self._nota = valor
    else:
      print("Nota deve ser entre 0 e 10.")

  @nota.deleter # deleter (opcional)
  def nota(self):
    pass