class ContaBancaria:
  """
  Cria uma conta bancária e permite fazer saques e depósitos.
  """

  def __init__(self, id, nome, saldo = 0):
    self.id = id # público (+)
    self._titular = nome # protegido (# ou _)
    self.__saldo = saldo # privado (- ou __)
    print(f"Conta {self.id} criada com sucesso. Saldo atual de R$ {self.__saldo:,.2f}")

  def __str__(self):
    return f"A conta {self.id} de {self._titular} tem R$ {self.__saldo:,.2f} de saldo"

  @property
  def titular(self):
    """Nome do titular (propriedade de leitura para compatibilidade)."""
    return self._titular

  @property
  def saldo(self):
    return self.__saldo

  @saldo.setter
  def saldo(self, valor):
    self.__saldo = valor
  
  def depositar(self, valor):
    valor = abs(valor) # Garante que o valor seja positivo
    self.saldo += valor
    print(f"Depósito de R$ {valor:,.2f} realizado com sucesso!")

  def sacar(self, valor):
    valor = abs(valor) # Garante que o valor seja positivo
    if valor > self.saldo:
      print(f"Saque NEGADO de R$ {valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE!")
    else:
      self.saldo -= valor
      print(f"Saque de R$ {valor:,.2f} realizado com sucesso!")