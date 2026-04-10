from rich import print, inspect
from classesex005 import Aluno, Professor, Funcionario

a1 = Aluno("José", 17, "Informática", "T101")
#inspect(a1, methods=True)

p1 = Professor("Maria", 35, "Matemática", "Doutorado")
#inspect(p1, methods=True)

f1 = Funcionario("Carlos", 28, "Secretário", "Administração")
#inspect(f1, methods=True)

a1.fazer_matricula()
p1.dar_aula()
f1.bater_ponto()