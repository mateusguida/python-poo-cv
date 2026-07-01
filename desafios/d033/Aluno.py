from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome: str, ano: int):
        super().__init__(nome, ano)
        self.cursos_oficiais = []
        self._curso = None

    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, curso: str):
        if curso in self.cursos_oficiais:
            self._curso = curso
        else:
            raise ValueError(f"Curso '{curso}' não é oficial.") 
    
    def add_curso(curso):
        pass