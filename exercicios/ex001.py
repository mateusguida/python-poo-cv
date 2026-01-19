# Declaração de Classe

class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1
    
    def mensagem(self):
        print(f"{self.nome} é Ganhafoto(a) e tem {self.idade} anos de idade.")
# Fim da Declaração de Classe

# Declaração de Objetos

g1 = Gafanhoto() # Instanciando o Objeto g1
g1.nome = "Maria"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto() # Instanciando o Objeto g2
g2.nome = "Mauro"
g2.idade = 53
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto() # Instanciando o Objeto g3
print(g3.mensagem())