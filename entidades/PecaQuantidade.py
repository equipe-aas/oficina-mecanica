class PecaQuantidade:
    def __init__(self, peca, quantidade):
        self.peca = peca
        self.quantidade = quantidade
    def str(self):
        string = "CODIGO "+str(self.peca.codigo)+" DESCRICAO: "+str(self.peca.descricao)+\
                 " QUANTIDADE: "+str(self.peca.quantidade) +"SUBTOTAL: R$ "+ round(self.quantidade*self.peca.preco_venda,2)
        return string