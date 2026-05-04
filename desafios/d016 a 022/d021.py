from rich import print

class Caneta:
    def __init__(self, cor="azul"):
        match cor.lower().strip():
            case "azul":
                self.cor = "[blue]"
            case "vermelha" | "vermelho":
                self.cor = "[red]"
            case "verde":
                self.cor = "[green]"
            case _:
                self.cor = "[white]"
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def tampar(self):
        self.tampada = True

    def escrever(self, texto):
        if self.tampada:
            print(f":prohibited: A {self.cor}caneta[/] está tampada!", end="")
        else:
            print(f"{self.cor}{texto}[/]", end="")
    
    def quebrar_linha(self, qtd=1):
      print("\n" * qtd, end="")

c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")
c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, Mundo! ")
c2.escrever("Funciona!")
c1.quebrar_linha(1)
c3.escrever("Deu certo! ")
c1.tampar()
c1.quebrar_linha(1)
c1.escrever("Será que rola?")
c2.quebrar_linha(1)