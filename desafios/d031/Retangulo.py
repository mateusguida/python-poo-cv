class Retangulo:
    def __init__(self, base=1, altura=1):
        self._base = base
        self._altura = altura
        self._area = base * altura

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, valor):
        if valor <= 0:
            raise ValueError("A base deve ser maior que zero.")
        self._base = valor
        self._area = self._base * self._altura

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        if valor <= 0:
            raise ValueError("A altura deve ser maior que zero.")
        self._altura = valor
        self._area = self._base * self._altura
    
    @property
    def area(self):
        return self._area
    
    @area.setter
    def area(self):
        raise TypeError("A área não pode ser alterada diretamente.")
    
    @property
    def medidas(self):
        return (f"Base: {self._base}, Altura: {self._altura}, Área: {self._area}")
    
    @medidas.setter
    def medidas(self, medidas):
        if len(medidas) == 2:
            if all(isinstance(m, (int, float)) for m in medidas) and all(m > 0 for m in medidas):
              self._base = medidas[0]
              self._altura = medidas[1]
              self._area = self._base * self._altura