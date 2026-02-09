from rich import print

class Funcionario:
    # Atributos de Classe
    empresa = "Curso em Vídeo"

    def __init__(self, nome, setor, cargo):
        # Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f":handshake: Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}"

c1 = Funcionario("Maria","Administração","Diretora")
# inspect(c1, methods=True)
print(c1.apresentacao())

c2 = Funcionario("Pedro","TI","Programador")
# inspect(c2, methods=True)
print(c2.apresentacao())

# inspect(Funcionario)