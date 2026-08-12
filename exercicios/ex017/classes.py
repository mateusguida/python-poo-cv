class Numero:
  def __init__(self, valor: int|float = 0):
    self.valor = valor

  def dobrar(self):
    self.valor *= 2

  def __str__(self):
    return f"Tenho o valor {self.valor} dentro do número."

class Texto:
  def __init__(self, txt: str = ""):
    self.txt = txt

  def dobrar(self):
    self.txt += self.txt

  def __str__(self):
    return f"Tenho o texto '{self.txt}' dentro do texto."

class Lista:
  def __init__(self, lst = []):
    self.lst = lst

  def dobrar(self):
    self.lst += self.lst

  def __str__(self):
    return f"Tenho os itens {self.lst} dentro da lista."

class Papel:
  def __init__(self):
    self.dobrado = False

  def dobrar(self):
    self.dobrado = True

  def __str__(self):
    return f"O papel está {'novo' if not self.dobrado else 'dobrado'}."

class Casa:
  def __init__(self):
    pass

  def __str__(self):
    return f"Era uma casa muito engraçada."

# DUCK TYPING

def tente_dobrar(obj):
  try:
    obj.dobrar()
  except:
    print(f"Tive dificuldade em dobrar o objeto {obj.__class__.__name__}.")