class Retangulo:
    def __init__(self, base=1, altura=1):
        # parametros privados, com None, para evitar erros de atribuição direta
        self._base = None
        self._altura = None
        self._area = None
        # inicializa os atributos usando os setters para validação
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("O valor da altura deve ser um número.")
        if valor < 0:
            raise ValueError("Valor inválido para a base.")
        else:
            self._base = valor

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("O valor da altura deve ser um número.")
        if valor < 0:
            raise ValueError("Valor inválido para a altura.")
        else:
            self._altura = valor
    
    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area
    
    @area.setter
    def area(self):
        raise PermissionError("A área não pode ser alterada diretamente.")
    
    @property
    def medidas(self):
        return (f"Base: {self.base}, Altura: {self.altura}, Área: {self.area}")
    
    @medidas.setter
    def medidas(self, valores:tuple):
        if not isinstance(valores, tuple):
            raise TypeError("As medidas devem ser passadas em uma tupla.")
        if len(valores) != 2:
            raise SyntaxError("A tupla deve conter exatamente dois valores: base e altura.")
        if isinstance(valores[0], (int, float)):
            self._base = valores[0]
        else:
            raise TypeError("O valor da base deve ser um número.")
        if isinstance(valores[1], (int, float)):
            self._altura = valores[1]
        else:
            raise TypeError("O valor da altura deve ser um número.")
        
