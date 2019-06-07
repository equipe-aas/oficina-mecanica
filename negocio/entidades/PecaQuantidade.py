class PecaQuantidade:
    def __init__(self, peca, quantidade):
        self.peca = peca
        self.preco_custo = peca.preco_custo
        self.preco_venda = peca.preco_venda
        self.quantidade = quantidade
    def __str__(self):
        string = "CODIGO "+str(self.peca.codigo)+" DESCRICAO: "+str(self.peca.descricao)+\
                 " QUANTIDADE: "+str(self.quantidade) +"SUBTOTAL: R$ "+ str(round(self.quantidade*self.preco_venda,2))
        return string
    def total(self):
        return round(self.quantidade*self.preco_venda,2)