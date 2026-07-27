from Pessoa import Pessoa

class Aluno(Pessoa):

    cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]

    def __init__(self, nome: str, ano: int, curso: str):
        super().__init__(nome, ano)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, curso: str):
        if curso in Aluno.cursos_oficiais:
            self._curso = curso
        else:
            raise ValueError(f"Curso '{curso}' não é oficial.") 
    
    def add_curso(self, curso: str):
        curso = curso.strip().upper()

        if 3 <= len(curso) <= 5:
            if curso not in Aluno.cursos_oficiais:
                Aluno.cursos_oficiais.append(curso)
                print(f"Curso '{curso}' adicionado com sucesso.")
            else:
                print(f"Curso '{curso}' já existe na lista de cursos oficiais.")
        else:
            raise ValueError(f"Curso '{curso}' não é válido. Deve ter entre 3 e 5 caracteres.")