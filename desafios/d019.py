from rich import print
import time
class Livro:
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.pagina_atual = 1
        print(f"\n:open_book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/red]' que tem [green] {self.total_paginas} páginas[/green] no total. Você agora está na [yellow]página {self.pagina_atual}[/yellow].\n")

    def avancar_paginas(self, num_paginas=1):
        if self.pagina_atual + num_paginas <= self.total_paginas:
            for p in range(num_paginas):
              print(f"Pág {self.pagina_atual + 1 + p} :arrow_forward:", end=" ")
              time.sleep(0.2)
            print(f"[blue] Você avançou {num_paginas} páginas e agora está na [yellow]página {self.pagina_atual + num_paginas}[/yellow].[/blue]\n")
            self.pagina_atual += num_paginas
        else:
            total_paginas_restantes = self.total_paginas - self.pagina_atual
            for p in range(total_paginas_restantes):
              print(f"Pág {self.pagina_atual + 1 + p} :arrow_forward:", end=" ")
            print(f"[blue] Você avançou {total_paginas_restantes} páginas e agora está na [yellow]página {self.total_paginas}[/yellow].[/blue]\n")
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/red]\n")

l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)  # Deve exibir uma mensagem de erro