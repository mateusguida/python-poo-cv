from Personagem import *

def main():
    p1 = Guerreiro("Kratos", 2000)
    p2 = Mago("Merlin", 3000)
    print()

    while p1.flag and p2.flag:
      p1.atacar(p2, 2000)
      if not p2.flag:
         break
      p2.curar()
      p2.atacar(p1, 2000)
      if not p1.flag:
         break
      p1.curar()

    print()

if __name__ == "__main__":
    main()