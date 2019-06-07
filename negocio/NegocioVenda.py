from db.ConexaoDataBase import ConexaoDataBase
from excessoes.CodigoNaoEncontradoException import CodigoNaoEncontradoException

class NegocioVenda:
    def __init__(self):
        self.vendas = ConexaoDataBase()
    def adicionar(self,venda):
        self.vendas.inserirVenda(venda)
    def remover(self,codigo):
        self.vendas.deletarVenda(codigo)
    def buscarVenda(self,codigo):
        venda = self.vendas.buscarVenda(codigo)
        if venda != None:
            return venda
        else:
            raise CodigoNaoEncontradoException(codigo)
    def __str__(self):
        string = ""
        for i in self.vendas.todasVendas():
            string += i.__str__()
        return string