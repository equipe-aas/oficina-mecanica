class ItemVenda:
    def __init__(self, quantidade, peca, servico):
        self.peca = peca
        self.servico = servico
        self.quantidade = quantidade
    def calcularTotal(self):
        if(self.peca != None):
            return round(self.quantidade*self.peca.preco_venda,2)
        else:
            return round(self.quantidade*self.servico.preco_venda,2)
    def __str__(self):
        string = ""
        if (self.peca != None):
            string += "DESCRICAO: "+self.peca.descricao+" QUANTIDADE: "+self.quantidade+\
                      " SUBTOTAL: R$ "+self.peca.preco_venda
        else:
            string += "DESCRICAO: "+self.servico.descricao+" QUANTIDADE: "+self.quantidade+\
                      " SUBTOTAL: R$ "+self.servico.preco_venda
        return string