class Carteira:

  def __init__(self, valor:int|float = 0):
    self.__saldo = valor

  def __str__(self):
    return f"Saldo: {self.__saldo:,.2f}"

  @property
  def saldo(self):
    return self.__saldo

  @saldo.setter
  def saldo(self, valor:int|float):
    raise PermissionError("Não é permitido alterar o saldo diretamente.")

  def __eq__(self, outro):
    if self.__saldo == outro.__saldo:
      return True
    else:
      return False

  def __iadd__(self, valor:int|float):
    self.__saldo += valor
    return self

  def __isub__(self, valor:int|float):
    self.__saldo -= valor
    return self