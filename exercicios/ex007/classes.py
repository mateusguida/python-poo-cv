from abc import ABC, abstractmethod # Abstract Base Class

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod # Método abstrato, deve ser implementado pelas subclasses
    def estudar(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} fez matrícula no curso de {self.curso}, turma {self.turma}.")

    def estudar(self):
        print(f"O aluno {self.nome} está estudando {self.curso} para a turma {self.turma}.")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O professor {self.nome} está dando aula de {self.especialidade}.")
    
    def estudar(self):
        print(f"O professor {self.nome} está estudando para aprimorar seus conhecimentos em {self.especialidade} e seu nível é {self.nivel}.")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} bateu ponto no setor {self.setor} como {self.cargo}.")
    
    def estudar(self):
        print(f"O funcionário {self.nome} está estudando para melhorar suas habilidades no cargo de {self.cargo} no setor {self.setor}.")