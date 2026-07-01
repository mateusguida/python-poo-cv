from Termostato import Termostato
from rich import print, inspect

def main():
  t = Termostato()
  try:
    t.temperatura = 25.2
  except Exception as e:
    print(f"Houve um problema: [red]{e}[/]")
  #inspect(t, methods=True, private=True)
  print(f"A temperatura atual é {t.ftemperatura}")

if __name__ == "__main__":
  main()