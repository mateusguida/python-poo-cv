from rich import print
from rich.panel import Panel

class Churrasco:
    # Atributos de classe
    consumo_padrao =0.400
    preco_kg = 82.40
    def __init__(self, nome_evento, num_pessoas):
        self.nome_evento = nome_evento
        self.num_pessoas = num_pessoas

    def __str__(self):
        return f"Esse é o evento {self.nome_evento} com {self.num_pessoas} convidados"

    def analisar(self):
        total_carne = self.num_pessoas * self.consumo_padrao
        custo_carne = total_carne * self.preco_kg

        conteudo = f"Analisando [green]{self.nome_evento}[/] com [blue]{self.num_pessoas} convidados[/]"
        conteudo += f"\nCada participante comerá 0.4 kg e cada kg custará R$ 82,40"
        conteudo += f"\nRecomendo [blue]comprar {total_carne:.3f} kg[/] de carne"
        conteudo += f"\nO custo total será de [green]R$ {custo_carne:,.2f}[/]"
        conteudo += f"\nCada pessoa pagará [yellow]R$ {custo_carne / self.num_pessoas:,.2f}[/] para participar"

        caixa = Panel(conteudo, title=self.nome_evento)
        print(caixa)

c1 = Churrasco("Churras dos Amigos", 15)
print(c1)
c1.analisar()

c2 = Churrasco("Festa do fim de ano", 80)
print(c2)
c2.analisar()