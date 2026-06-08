from ex010 import Avaliacao
from rich import print, inspect

def main():
  av1 = Avaliacao("Pedro", "Matemática")
  #av1.nota = -2.0 # Tentativa de definir uma nota inválida
  av1.nota = 8.5 # Definindo uma nota válida
  print(f"{av1.nome} tirou {av1.nota} em {av1.disciplina}")
  #inspect(av1, private=True)

if __name__ == "__main__":
  main() 