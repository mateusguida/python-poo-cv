from abc import ABC, abstractmethod
import random
from rich import print

class Personagem(ABC):
    
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.flag = True
        self.golpes = []

    def atacar(self, alvo: 'Personagem', forca: int):
        golpe = random.choice(self.golpes)
        print(f"[green]{self.nome}[/] ([orange]{self.vida:.0f}[/]) atacou [red]{alvo.nome}[/] ([orange]{alvo.vida:.0f}[/]) com um [blue]{golpe}[/] de força [orange]{forca}[/]!")
        print(alvo.receber_dano(forca))

    def receber_dano(self, dano: int):
        dado = random.randint(1, 100)
        texto = f"[blue]{self.nome}[/] recebeu [red]dano de {dano/dado:.0f}[/]!"
        self.vida -= dano/dado
        if self.vida <= 0:
            texto += f"\n[red]{self.nome} foi derrotado![/]"
            self.flag = False
        return(texto)
    
    @abstractmethod
    def curar():
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Corte", "Golpe", "Soco"]

    def curar(self):
        dado = random.randint(1, 100)
        self.vida += dado
        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {dado} pontos[/] de vida!")

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Sopro de Fogo", "Raio Elétrico", "Jato Congelante"]

    def curar(self):
        dado = random.randint(1, 100)
        self.vida += dado
        print(f"[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {dado} pontos[/] de vida!")