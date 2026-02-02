from rich import print

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def tampar(self):
        self.tampada = True

    def escrever(self, texto):
        if self.tampada:
            print(":stop: A caneta está tampada!")
        else:
            if self.cor == "azul":
                print(f"[blue]{texto}[/blue]", end="")
            elif self.cor == "vermelha":
                print(f"[red]{texto}[/red]", end="")
            elif self.cor == "verde":
                print(f"[green]{texto}[/green]", end="")
            else:
                print(texto, end="")
    def quebrar_linha(self, n):
      for _ in range(n):
        print()

c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta('verde')

#c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem? ")
c1.quebrar_linha(2)
c2.escrever("Olá, Gafanhoto! ")
c3.escrever("Vamos exercitar!")