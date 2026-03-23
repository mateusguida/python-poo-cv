from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, usuario):
        self.nome = nome
        self.usuario = usuario
        self.favoritos = []

    def add_favoritos(self, jogo):
        self.favoritos.append(jogo)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        jogos = "Jogos favoritos:"
        for j in range(len(self.favoritos)):
            jogos += f"\n:video_game: [blue]{self.favoritos[j]}[/]"
        caixa = Panel(f"Nome real: [black on blue]{self.nome}[/]\n{jogos}", title=f"Jogador <{self.usuario}>",expand=False)
        print(caixa)

j1 = Gamer("Fabrício da Silva", "detonator2025")
j1.add_favoritos("Marios Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()

j2 = Gamer("Olivia Souza", "peach_raivosa")
j2.add_favoritos("The Last of Us")
j2.add_favoritos("GTA V")
j2.add_favoritos("Red Dead Redemption 2")
j2.ficha()