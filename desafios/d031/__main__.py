from rich import inspect, print
from Retangulo import Retangulo

def main():
  r = Retangulo()
  try:
    r.altura = 7
    r.base = 12
    r.medidas = (3,9)
  except Exception as e:
    print(f"Ocorreu um erro do tipo {type(e).__name__}: {e}")

  #inspect(r, methods=True, private=True)
  
  print(r.medidas)

if __name__ == "__main__":
  main()