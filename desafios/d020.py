from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, usuario):
        self.nome = nome
        self.usuario = usuario
        self.favoritos = []

    def add_favoritos(self, jogo):
        self.favoritos.append(jogo)
        self.favoritos.sort()

    def ficha(self):
        jogos = "Jogos favoritos:"
        for j in range(len(self.favoritos)):
            jogos += f"\n:joystick: {self.favoritos[j]}"
        caixa = Panel(f"Nome real: [blue]{self.nome}[/blue]\n{jogos}", title=f"Jogador <{self.usuario}>",expand=False)
        print(caixa)

j1 = Gamer("Fabrício da Silva", "detonator2025")
j1.add_favoritos("Marios Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()