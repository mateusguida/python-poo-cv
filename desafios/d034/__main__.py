from classes import *

def main():
  funcionarios = [
    Desenvolvedor("Pedro", 18_000),
    Designer("José", 25_000),
    Gerente("Mariana", 45_000)
  ]

  for f in funcionarios:
    print(f)
  
  try:
    f.salario = 2_000
  except Exception as e:
    print(f"Erro: {e}")

if __name__ == "__main__":
  main()