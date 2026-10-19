from classes import *

def main():
  validar_dados(Usuario(), "guanabara_123")
  validar_dados(Usuario(), "guanabara 123")

  validar_dados(Email(), "guanabara@gmail.com")
  validar_dados(Email(), "guanabaraoutlook.com")
  validar_dados(Email(), "guanabara@outlook,com")
  validar_dados(Email(), "@guanabaraaoutlook.com")

  validar_dados(Senha(), "123456")
  validar_dados(Senha(), "123456Ac#")
  validar_dados(Senha(), "123456Ac")
  validar_dados(Senha(), "123456A#")

if __name__ == "__main__":
  main()