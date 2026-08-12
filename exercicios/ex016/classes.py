class Porta:
  def abrir(self):
    print(f"Abra a porta para entrar.")

class Empresa:
  def abrir(self):
    print(f"Vá ao Portal do Empreendedor para abrir sua empresa.")

class Ovo:
  def abrir(self):
    print(f"Quebre o ovo para abrir.")

class Pedra:
  pass

# METODO DUCK TYPING

def tentar_abrir(obj):
  try:
    obj.abrir()
  except AttributeError:
    print(f"Não é possível abrir o objeto {obj.__class__.__name__}.")