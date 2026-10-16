from classes import *

def main():
  finalizar_compra(Pix(), 324.20)
  finalizar_compra(CartaoCredito(), 1324.20)
  finalizar_compra(Boleto(), 2324.20)

if __name__ == "__main__":
  main()