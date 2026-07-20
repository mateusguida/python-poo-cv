from rich import inspect, print
from ContaBancaria import ContaBancaria

def main():
  print("Criando a conta...")
  cc = ContaBancaria(111, "Josenildo", 10000)
  
  #inspect(cc, methods=True, private=True, title="Conta Bancária")
  
  print("Vou tentar sacar...")
  cc.sacar(500)

  print("Tentando mudar o nome...")
  cc.nome = "Josenildo da Silva"

  print(cc)

if __name__ == "__main__":
  main()