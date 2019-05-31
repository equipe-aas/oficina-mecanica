class RepositorioVenda:
    def __init__(self):
        self.vendas = []
    def adicionar(self,venda):
        self.vendas.append(venda)
    def remover(self,venda):
        self.vendas.remove(venda)
    def buscar(self,codigo):
        venda = None
        for v in self.vendas:
            if v.codigo == codigo:
                venda = v
                break
        return venda
    def __str__(self):
        string = ""
        for v in self.vendas:
            string += v.str() + "\n"
        return string
