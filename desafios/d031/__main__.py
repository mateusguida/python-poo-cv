from rich import inspect, print
from Retangulo import Retangulo

def main():
  r = Retangulo(8,4)
  r.altura = 12
  r.base = 5
  r.medidas = (-9, 3)
  inspect(r, methods=True, private=True)
  print(r.medidas)

  #try:
    #r.area = 23
  #except TypeError as e:
    #print(f"[red]Erro: {e}[/red]")

if __name__ == "__main__":
  main()