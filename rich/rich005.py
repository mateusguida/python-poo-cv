from rich.traceback import install
install()

def divisao(x,y):
  return x / y

print(divisao(50,0))

# visualização do erro muito melhor feita com rich.traceback.install()