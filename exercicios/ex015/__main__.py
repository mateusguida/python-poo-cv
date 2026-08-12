from classes import *

def main():
  c1 = Carteira(100)
  c2 = Carteira(200)

  print(c1 == c2)

  c1 += 50
  c1 -= 10
  print(c1)

if __name__ == "__main__":
  main()