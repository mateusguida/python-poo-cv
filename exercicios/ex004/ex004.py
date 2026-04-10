from rich import print, inspect

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} fez matrícula no curso de {self.curso}, turma {self.turma}.")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O professor {self.nome} está dando aula de {self.especialidade}.")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} bateu ponto no setor {self.setor} como {self.cargo}.")
    

a1 = Aluno("José", 17, "Informática", "T101")
inspect(a1, methods=True)

p1 = Professor("Maria", 35, "Matemática", "Doutorado")
inspect(p1, methods=True)

f1 = Funcionario("Carlos", 28, "Secretário", "Administração")
inspect(f1, methods=True)

a1.fazer_matricula()
p1.dar_aula()
f1.bater_ponto()