from rich import print

class Diario:
  def __init__(self, senhamestra = 'CeV!@'):
    self.__segredos = []
    self.__senha = senhamestra.strip()

  @property
  def senha(self):
    raise PermissionError("Ninguém tem a permissão de ver a senha")
  
  @senha.setter
  def senha(self, novasenha):
    senha_antiga = input(f"Digite a senha antiga para alterar a senha do diário: ")
    if senha_antiga != self.__senha:
      raise PermissionError("[red]Senha antiga incorreta! Você não pode alterar a senha do diário![/]")
    else:
      self.__senha = novasenha.strip()
      print(f"[green]Senha alterada com sucesso![/]")

  def escrever(self, msg):
    if isinstance(msg, str) and len(msg) > 0:
      self.__segredos.append(msg.strip())

  def ler(self, senha = None):
    if senha != self.__senha:
      raise PermissionError("Senha inválida! Você não pode ler meu diário!")
    else:
      print(f"[green]Diário LIBERADO![/]")
      for msg in self.__segredos:
        print(f" - {msg}")
      print()