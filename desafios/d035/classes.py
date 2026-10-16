from abc import ABC, abstractmethod

class Arquivo(ABC):
  def __init__(self, nome: str, ext:str, tamanho: int = 0):
    self.nome = nome
    self.tamanho = tamanho
    self._extensao = None
    self.extensao = ext

  @abstractmethod
  def abrir(self):
    pass

  @property
  def extensao(self):
    return self._extensao

  @extensao.setter
  def extensao(self, ext:str):
    formatos = ['pdf','doc']
    ext = ext.lower().strip()
    if ext in formatos:
      self._extensao = ext
    else:
      raise AttributeError("O arquivo está em um formato não suportado.")

  @property
  def nome_completo(self):
    return f"'{self.nome}.{self._extensao}' ({self.tamanho/1_000_000:.2f}MB)"

  def __str__(self):
    return f"{self.nome_completo}"

class DOC(Arquivo):
  def __init__(self, nome: str, tamanho: int):
    super().__init__(nome, 'doc', tamanho)

  def abrir(self):
    print(f"Abrindo {self.nome_completo} no Word.")

class PDF(Arquivo):
  def __init__(self, nome: str, tamanho: int):
    super().__init__(nome, 'pdf', tamanho)

  def abrir(self):
    print(f"Abrindo {self.nome_completo} no Acrobat.")

def abrir_arquivo(arquivo: Arquivo):
    arquivo.abrir()