class ContaBancaria:
    def __init__(self, id, titular, saldo=0):
        self._id = id
        self._titular = titular
        self.__saldo = saldo
        self.__hash = None
        print(f"Conta {self._id} criada com sucesso. Saldo atual de R$ {self.__saldo}")
    
    @property
    def id(self):
        return self._id
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self.__saldo = valor

    @property
    def nome(self):
        return self._titular

    @property
    def hash(self):
        return self.__hash
    
    def validar_senha(self, chave: str) -> bool:
        # Implementação da validação da senha
        pass
    
    def pede_senha(self) -> str:
        # Implementação para pedir a senha do usuário
        pass
    
    def sacar(valor: float, chave: str = None):
        pass
    
    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depósito de R$ {valor} autorizado na conta {self._id}")