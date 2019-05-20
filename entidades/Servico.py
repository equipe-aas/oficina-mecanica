class Servico:
    def __init__(self, codigo, descricao, preco_venda, peca = None):
        self.codigo = codigo
        self.descricao = descricao
        self.peca = peca
        self.preco_venda = preco_venda
    def str(self):
        string = "CODIGO : " + str(self.codigo) + "\nDESCRICAO: " + str(self.descricao) +\
                 "\nPRECO DE VENDA: R$ " + str(round(self.preco_venda, 2))
        if(self.peca != None):
            string += self.peca.str()
        return string
