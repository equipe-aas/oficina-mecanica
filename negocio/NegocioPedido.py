from dados.RepositorioPedido import RepositorioPedido
from excessoes.CodigoJaExisteException import CodigoJaExisteException
from excessoes.CodigoNaoEncontradoException import CodigoNaoEncontradoException

class NegocioPedido:
    def __init__(self):
        self.pedidos = RepositorioPedido()
    def adicionar(self,pedido):
        if(self.pedidos.buscar(pedido.codigo)):
            self.pedidos.adicionar(pedido)
        else:
            raise CodigoJaExisteException(pedido.codigo)
    def remover(self,codigo):
        pedido = self.pedidos.buscar(codigo)
        if(pedido != None):
            self.pedidos.remover(pedido)
        else:
            raise CodigoNaoEncontradoException(pedido.codigo)
    def buscar(self,codigo):
        pedido = self.pedidos.buscar(codigo)
        if (pedido != None):
            return pedido
        else:
            raise CodigoNaoEncontradoException(pedido.codigo)
    def str(self):
        return self.pedidos.str()