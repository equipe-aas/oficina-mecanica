from excessoes.CodigoNaoEncontradoException import CodigoNaoEncontradoException
from db.ConexaoDataBase import ConexaoDataBase

class NegocioPedido:
    def __init__(self):
        self.pedidos = ConexaoDataBase()
    def adicionar(self,pedido):
        self.pedidos.inserirPedido(pedido)
    def remover(self,codigo):
        pedido = self.pedidos.buscarPedido(codigo)
        if(pedido != None):
            self.pedidos.deletarPedido(codigo)
        else:
            raise CodigoNaoEncontradoException(codigo)
    def buscar(self,codigo):
        pedido = self.pedidos.buscarPedido(codigo)
        if (pedido != None):
            return pedido
        else:
            raise CodigoNaoEncontradoException(codigo)
    def all_pedidos(self):
        return self.pedidos.todosPedidos()
    def __str__(self):
        string = ""
        for i in self.pedidos.todosPedidos():
            string += i.__str__()
        return string