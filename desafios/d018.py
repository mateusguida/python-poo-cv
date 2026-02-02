from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, nome_evento, num_pessoas):
        self.nome_evento = nome_evento
        self.num_pessoas = num_pessoas

    def analisar(self):
        total_carne = self.num_pessoas * 0.4  # kg por pessoa
        custo_carne = total_carne * 82.40  # R$ 82,40 por kg

        caixa = Panel(f"Analisando [green]{self.nome_evento}[/green] com [blue]{self.num_pessoas} convidados[/blue]\nCada participante comerá 0.4 kg e cada kg custará R$ 82,40\nRecomendo [blue]comprar {total_carne:.3f} kg[/blue] de carne\nO custo total será de [green]R$ {custo_carne:.2f}[/green]\nCada pessoa pagará [yellow]R$ {custo_carne / self.num_pessoas:.2f}[/yellow] para participar", title = self.nome_evento)
        print(caixa)

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()