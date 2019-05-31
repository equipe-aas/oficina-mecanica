from dados.RepositorioPessoa import RepositorioPessoa
from excessoes.CpfJaExisteException import CpfJaExisteException
from excessoes.CpfNaoEncontradoException import CpfNaoEncontradoException
from excessoes.CpfInvalidoException import CpfInvalidoException
from excessoes.NomeInvalidoException import NomeInvalidoException
from excessoes.TelefoneInvalidoException import TelefoneInvalidoException
from entidades.Cliente import Cliente

class NegocioCliente:
    def __init__(self):
        self.clientes = RepositorioPessoa()
    def adicionar(self, cpf, nome, endereco, telefone):
        if not self.isCpf(cpf):
            raise CpfInvalidoException(cpf)
        if(self.clientes.buscar(cpf) != None):
            raise CpfJaExisteException(cpf)
        if len(nome)<10:
            raise NomeInvalidoException(nome)
        if len(telefone < 8):
            raise TelefoneInvalidoException(telefone)
        else:
            self.clientes.adicionar(Cliente(cpf, nome, endereco, telefone))
    def remover(self, cpf):
        cliente = self.clientes.buscar(cpf)
        if(cliente != None):
            self.clientes.remover(cliente)
        else:
            raise CpfNaoEncontradoException(cpf)
    def buscar(self, cpf):
        cliente = self.clientes.buscar(cpf)
        if(cliente != None):
            return cliente
        else:
            raise CpfNaoEncontradoException(cpf)
    def __str__(self):
        return self.clientes.__str__()
    def isCpf(self, cpf):
        if(len(cpf) < 11):
            return False

        n = ['0','1','2','3','4','5','6','7','8','9']
        for i in list(cpf):
            if(i not in n):
                return False
        return True
