from classes import *

def main():
  x = Analisador()
  x.analisar(3)
  x.analisar("Olá, Mundo")
  x.analisar(3.14)
  x.analisar([1,2,3])
  x.analisar((4,5,6))
  x.analisar({"a": 1, "b": 2})
  x.analisar(max([6,9,12]))

if __name__ == "__main__":
  main()