from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome: str, ano: int):
        self._nome = nome
        self._nascimento = ano

    @property
    def idade(self):
        return date.today().year - self._nascimento

    @property
    def nascimento(self):
        return self._nascimento