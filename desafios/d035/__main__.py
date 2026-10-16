from classes import *

def main():
  a1 = DOC("prova", 1_200_000)
  a2 = PDF("contrato", 850_000)

  abrir_arquivo(a1)
  abrir_arquivo(a2)

if __name__ == "__main__":
  main()