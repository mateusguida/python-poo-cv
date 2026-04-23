from Transporte import *
from rich import print
from rich.table import Table

def main():
    dist = 10
    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]
    
    print()
    tabela = Table(title="Tabela de Fretes")

    tabela.add_column("Distância", justify="left")
    tabela.add_column("Tipo", justify="left")
    tabela.add_column("Frete", justify="left")

    for i in range(len(viagem)):
        entrega = viagem[i]
        tabela.add_row(f"{dist} km", f"{type(entrega).__name__}", f"{entrega.calc_frete()}")

    print(tabela)
    print()

if __name__ == "__main__":
    main()