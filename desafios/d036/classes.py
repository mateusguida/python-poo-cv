from abc import ABC, abstractmethod
import locale

class Pagamento(ABC):
  def __init__(self):
    self._valor = None

  @property
  def valor(self):
    return self._valor

  @valor.setter
  def valor(self, valor: float):
    if valor <= 0:
      raise ValueError("O valor do pagamento deve ser maior que zero.")
    self._valor = valor

  # Fazendo a localização monetária para o Brasil, usando a biblioteca locale
  @property
  def fvalor(self):
    #return f"R$ {self._valor:,.2f}"
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(self._valor, grouping=True)

  @abstractmethod
  def pagar(self):
    pass

class Boleto(Pagamento):
  def pagar(self, valor: float):
    try:
      self.valor = valor
      #Código de pagamento do boleto
      return f"Pagamento de {self.fvalor} realizado com sucesso via Boleto."
    except Exception as e:
      return f"Erro ao processar o pagamento de {self.fvalor} via Boleto: {e}"

class Pix(Pagamento):
  def pagar(self, valor: float):
    try:
      self.valor = valor
      #Código de pagamento do Pix
      return f"Pagamento de {self.fvalor} realizado com sucesso via Pix."
    except Exception as e:
      return f"Erro ao processar o pagamento de {self.fvalor} via Pix: {e}"

class CartaoCredito(Pagamento):
  def pagar(self, valor: float):
    try:
      self.valor = valor
      #Código de pagamento do Cartão de Crédito
      return f"Pagamento de {self.fvalor} realizado com sucesso via Cartão de Crédito."
    except Exception as e:
      return f"Erro ao processar o pagamento de {self.fvalor} via Cartão de Crédito: {e}"

def finalizar_compra(pagamento: Pagamento, valor: float):
  print(pagamento.pagar(valor))