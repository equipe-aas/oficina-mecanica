from dados.RepositorioPessoa import RepositorioPessoa
from excessoes.CpfJaExisteException import CpfJaExisteException
from excessoes.CpfNaoEncontradoException import CpfNaoEncontradoException

class NegocioCliente:
    def __init__(self):
        self.clientes = RepositorioPessoa()
    def adicionar(self,cliente):
        if(self.clientes.buscar(cliente.cpf) != None):
            self.adicionar(cliente)
        else:
            raise CpfJaExisteException(cliente.cpf)
    def remover(self,cpf):
        cliente = self.clientes.buscar(cpf)
        if(cliente != None):
            self.clientes.remover(cliente)
        else:
            raise CpfNaoEncontradoException(cpf)
    def buscar(self,cpf):
        cliente = self.clientes.buscar(cpf)
        if(cliente != None):
            return cliente
        else:
            raise CpfNaoEncontradoException(cpf)
    def str(self):
        return self.clientes.str()