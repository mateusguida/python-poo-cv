from rich import print, inspect
from classes import Aluno, Professor, Funcionario

def main():
    a1 = Aluno("José", 17, "Informática", "T101")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    #inspect(a1, methods=True)

    p1 = Professor("Maria", 35, "Matemática", "Doutorado")
    p1.fazer_aniversario()
    p1.dar_aula()
    #inspect(p1, methods=True)

    f1 = Funcionario("Carlos", 28, "Secretário", "Administração")
    f1.fazer_aniversario()
    f1.bater_ponto()
    #inspect(f1, methods=True)

    a1.estudar()
    p1.estudar() 
    f1.estudar()

if __name__ == "__main__":
    main()