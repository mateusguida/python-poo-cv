from functools import singledispatchmethod

class Analisador:

  @singledispatchmethod
  def analisar(self, valor):
    print(f"Tipo de valor não suportado: {valor}")

  @analisar.register
  def _(self, valor: int):
    print(f"{valor} é um número inteiro.")

  @analisar.register
  def _(self, valores: str):
    print(f"'{valores}' é uma cadeia de caracteres.")

  @analisar.register
  def _(self, valor: float):
    print(f"{valor} é um número de ponto flutuante.")

  @analisar.register
  def _(self, valor: tuple|dict|list):
    print(f"{valor} é uma coleção de dados.")