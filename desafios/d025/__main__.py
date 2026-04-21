from Transporte import *
from rich import print

def main():
    dist = 8

    # entrega = Moto(dist, 0)
    # entrega = Caminhao(dist, 0)
    entrega = Drone(dist, 0)
    print(f"Frete de {type(entrega).__name__} em {dist} km = {entrega.calc_frete()}")

if __name__ == "__main__":
    main()