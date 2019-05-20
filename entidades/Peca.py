class Peca:
    def __init__(self, codigo, descricao, fornecedor, preco_custo, preco_venda, quantidade):
        self.codigo = codigo
        self.descricao = descricao
        self.fornecedor = fornecedor
        self.preco_custo = preco_custo
        self.preco_venda = preco_venda
        self.quantidade = quantidade
    def str(self):
        string = "CODIGO : "+str(self.codigo)+"\nDESCRICAO: "+str(self.descricao)+\
                 "\nPRECO DE CUSTO: R$ "+str(round(self.preco_custo,2))+"\nPRECO DE VENDA: R$ "+str(round(self.preco_venda,2))+\
                 "\nQUANTIDADE: "+str(self.quantidade)+"\n"+self.fornecedor.str()
        return string