from dados.RepositorioVenda import RepositorioVenda
from excessoes.CodigoNaoEncontradoException import CodigoNaoEncontradoException

class NegocioVenda:
    codigo = 0
    def __init__(self):
        self.vendas = RepositorioVenda()
    def adicionar(self,venda):
        self.vendas.adicionar(venda)
    def remover(self,codigo):
        self.vendas.remover(self.buscar(codigo))
    def buscar(self,codigo):
        venda = self.vendas.buscar(codigo)
        if venda != None:
            return venda
        else:
            raise CodigoNaoEncontradoException(codigo)
    def __str__(self):
        return self.vendas.__str__()
