from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    def __init__(self, nome: str):
        self.nome = nome
        self.sal_min = 1612.00
        self.inss = 7.5

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        print()
        
        texto = f"O salário de [blue]{self.nome}[/] ([purple]{type(self).__name__}[/]) é de [green]R$ {self.calcular_salario():.2f}[/green] e corresponde a [yellow]{self.calcular_salario() / self.sal_min:.1f} salários mínimos[/]."

        caixa = Panel(texto, title="Análise de Salário", width=50)
        
        print(caixa)
        
        print()
    
class Horista(Funcionario):
    def __init__(self, nome: str, valor_hora: float, horas_trab: int):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trab

    def calcular_salario(self):
        return (1 - self.inss / 100) * (self.horas_trabalhadas * self.valor_hora)

class Mensalista(Funcionario):
    def __init__(self, nome: str, sal_bruto: float):
        super().__init__(nome)
        self.valor_mes = sal_bruto

    def calcular_salario(self):
        return self.valor_mes * (1 - self.inss / 100)