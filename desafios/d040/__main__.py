from classes import *

def main():
  u = [
    Usuario("Maria", "maria@gmail.com"),
    Usuario("João", "joao@hotmail.com"),
    Usuario("Ana", "ana@me.com")
  ]

  a = [
    Aluno("Pedro", "Informática" , "4º período"),
    Aluno("Clara", "ADS" , "8º período")
  ]

  exportar_dados(XML(), u)
  exportar_dados(XML(), a)
  exportar_dados(JSON(), u)
  exportar_dados(JSON(), a)

if __name__ == "__main__":
  main()