from rich import print
from poligono import poligono
from quadrado import quadrado
from circulo import circulo

def main():
    p1 = quadrado(12)

    print(f"Perímetro do quadrado: [green]{p1.perimetro():.1f}")
    print(f"Área do quadrado: [green]{p1.area():.1f}")

    p2 = circulo(20)

    print(f"Perímetro do círculo: [green]{p2.perimetro():.1f}")
    print(f"Área do círculo: [green]{p2.area():.1f}")

if __name__ == "__main__":
    main()