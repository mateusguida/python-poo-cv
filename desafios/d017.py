from rich import print
from rich.panel import Panel
from rich.align import Align

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        intervalo = "-" * 30
        valor = f'R$ {self.preco:.2f}'
        preco = f"{'.' * ((30 - len(valor))//2)}{valor}{'.' * ((30-len(valor))//2)}"
        caixa = Panel(f"{self.nome}\n{intervalo}\n {preco}", title="Produto", width=35)
        print(caixa)

p1 = Produto("iPhone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8_000)

p1.etiqueta()
p2.etiqueta()