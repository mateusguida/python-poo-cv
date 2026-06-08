class Avaliacao:
  def __init__(self, nome, disciplina, nota = 0.0):
    self.nome = nome
    self.disciplina = disciplina
    self._nota = nota

  # Métodos de acesso (getters e setters)
  def get_nota(self): # Método getter para acessar a nota
    return self._nota

  def set_nota(self, valor): # Método setter para modificar a nota
    if 0 <= valor <= 10:
      self._nota = valor
    else:
      print("Nota deve ser entre 0 e 10.")