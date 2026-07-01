from rich import inspect, print
from Diario import Diario

def main():
  d = Diario("Gafanhoto")

  d.escrever("Primeira mensagem")
  d.escrever("Você é uma pessoa simpática")
  d.escrever("Você gosta de Python")

  try:
    d.ler("Gafanhoto")
  except PermissionError as e:
    print(f"[red]{e}[/]")

  try:
    d.senha = "Guanabara"
  except PermissionError as e:
    print(f"[red]{e}[/]")

  #inspect(d, methods=True, private=True, title="Diário")


if __name__ == "__main__":
  main()