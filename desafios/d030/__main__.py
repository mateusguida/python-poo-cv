from rich import inspect, print
from Credencial import Credencial

def main():
  c = Credencial()
  c.senha = "CeV!@"
  print(c.senha)

  c.validar("Curso123")
  c.validar("CeV!@")

  # inspect(c, methods=True, private=True, title="Credencial")

if __name__ == "__main__":
  main()