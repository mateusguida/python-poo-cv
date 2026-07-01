from rich import inspect, print
from ContaBancaria import ContaBancaria

def main():
  print("Criando a conta...")
  cc = ContaBancaria(123, "Gustavo", 1000)
  #inspect(cc, methods=True, private=True, title="Conta Bancária")

  print("Realizando depósito")
  cc.depositar(500)

if __name__ == "__main__":
  main()