# Declaração de Classe

class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
    Para criar uma nova pessa, use a seguinte sintaxe:
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, n = "Vazio", i = 0): # Método Construtor
        # Atributos de Instância
        self.nome = n
        self.idade = i

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1
    
    def __str__(self):
        return f"{self.nome} é Ganhafoto(a) e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}."
    
# Fim da Declaração de Classe

# Declaração de Objetos

g1 = Gafanhoto("Maria", 17) # Instanciando o Objeto g1
g1.aniversario()
print(g1)
# print(g1.__doc__) # Dunder Attibute
# print(g1.__dict__) # Exibição em forma de dicionário - Atributo
# print(g1.__getstate__()) # Exibição em forma de dicionário - Método
# print(g1.__class__) # Exibição da Classe do Objeto

g2 = Gafanhoto("Mauro", 53) # Instanciando o Objeto g2
g2.aniversario()
print(g2)

g3 = Gafanhoto() # Instanciando o Objeto g3
print(g3)