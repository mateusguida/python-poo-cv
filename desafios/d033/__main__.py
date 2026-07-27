from rich import inspect, print
from Pessoa import Pessoa
from Aluno import Aluno

def main():
  # p = Pessoa("Mateus", 1986)
  # p.idade = 90
  # print(p.idade)

  a = Aluno("Mateus", 1986, 'ADM')
  a.add_curso("MODA")

  inspect(a, methods=True, private=True, title="Aluno")

  a.add_curso("KKKKKKKKK")

if __name__ == "__main__":
  main()