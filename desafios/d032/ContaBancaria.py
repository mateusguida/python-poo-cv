from hashlib import sha256

class ContaBancaria:
  """
  Cria uma conta bancária e permite fazer saques e depósitos.
  """

  def __init__(self, id:int, nome:str = None, saldo:float = 0, chave:str = None):
    self._id = id # protegido
    self._titular = nome # protegido
    self.__saldo = saldo # privado
    if chave is None:
      chave = self.pede_senha()
    self.__hash = sha256(chave.encode()).hexdigest() # privado
    print(f"Conta {self._id} criada com sucesso. Saldo atual de R$ {self.__saldo:,.2f}")

  def pede_senha(self) -> str:
    from pwinput import pwinput # leitura de password sem exibir na tela
    while True:
      senha = str(pwinput("Digite a senha da conta (mínimo 6 caracteres): ")).strip()
      if len(senha) >= 6:
        break
    return senha
  
  def validar_senha(self, chave:str) -> bool:
    return sha256(chave.encode()).hexdigest() == self.__hash

  def __str__(self):
    return f"A conta {self._id} de {self._titular} tem R$ {self.__saldo:,.2f} de saldo"

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

  def sacar(self, valor:float, chave:str = None):
    valor = abs(valor) # Garante que o valor seja positivo
    if chave is None:
      chave = self.pede_senha()
    if self.validar_senha(chave):
      if valor > self.saldo:
        print(f"Saque NEGADO de R$ {valor:,.2f} na conta {self._id}: SALDO INSUFICIENTE!")
      else:
        self.saldo -= valor
        print(f"Saque de R$ {valor:,.2f} realizado com sucesso!")
    else:
      print(f"Saque NEGADO de R$ {valor:,.2f} na conta {self._id}: SENHA INVÁLIDA!")

  @property
  def nome(self):
    """Nome do titular (propriedade de leitura para compatibilidade)."""
    return self._titular
  
  @nome.setter
  def nome(self, novonome:str = None):
      chave = self.pede_senha()
      if self.validar_senha(chave):
          if len(novonome) >= 5:
              self._titular = novonome
          print(f"Nome do titular alterado com sucesso para {self._titular}!")
      else:
          print("Alteração de nome NEGADA: SENHA INVÁLIDA!")