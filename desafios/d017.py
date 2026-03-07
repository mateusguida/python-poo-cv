from rich import print
from rich.panel import Panel
from rich.align import Align

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += "-" * 30
        valor = f'R$ {self.preco:,.2f}'
        conteudo += f"\n{valor.center(30, ' ')}"
        etiqueta = Panel(conteudo, title="Produto", width=34)
        print(etiqueta)

p1 = Produto("iPhone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8_000)

p1.etiqueta()
p2.etiqueta()