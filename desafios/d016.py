from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f":right-facing_fist: Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da empresa Curso em Vídeo."

c1 = Funcionario("Maria","Administração","Diretora")
print(c1.apresentacao())

c2 = Funcionario("Pedro","TI","Programador")
print(c2.apresentacao())