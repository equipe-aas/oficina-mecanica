class RepositorioPedido:
    def __init__(self):
        self.pedidos = []
    def adicionar(self,pedido):
        self.pedidos.append(pedido)
    def remover(self,pedido):
        self.pedidos.remove(pedido)
    def buscar(self,codigo):
        pedido = None
        for p in self.pedidos:
            if p.codigo == codigo:
                pedido = p
                break
        return pedido
    def str(self):
        string = ""
        for p in self.pedidos:
            string += p.str() + "\n"
        return string
