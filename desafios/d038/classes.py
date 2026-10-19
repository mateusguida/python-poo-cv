class Produto:
    def __init__(self, nome:str, preco:float = 0.0):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} ({formata_dinheiro(self.preco)})"

class Carrinho:
    def __init__(self, produtos:list=None):
        self.produtos = produtos if produtos else []

    def __add__(self, other):
        if isinstance(other, Produto):
            return Carrinho(self.produtos + [other])
        elif isinstance(other, Carrinho):
            return Carrinho(self.produtos + other.produtos)
        else:
            raise TypeError("Você só pode adicionar um Produto ou outro Carrinho.")

    def __str__(self):
        linha = "\n" + "-" * 30
        itens = "\n".join(str(produto) for produto in self.produtos)
        return f"{linha}\n{itens}{linha}\nTotal: {formata_dinheiro(self.total)}"

    @property
    def total(self):
        return sum(produto.preco for produto in self.produtos)

def formata_dinheiro(valor: float):
    import locale
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(valor, grouping=True)