from dados.RepositorioPessoa import RepositorioPessoa
from excessoes.CpfJaExisteException import CpfJaExisteException
from excessoes.CpfNaoEncontradoException import CpfNaoEncontradoException

class NegocioCliente:
    def __init__(self):
        self.funcionarios = RepositorioPessoa()
    def adicionar(self,funcionario):
        if(self.funcionarios.buscar(funcionario.cpf) != None):
            self.adicionar(funcionario)
        else:
            raise CpfJaExisteException(funcionario.cpf)
    def remover(self,cpf):
        funcionario = self.funcionarios.buscar(cpf)
        if(funcionario != None):
            self.funcionarios.remover(funcionario)
        else:
            raise CpfNaoEncontradoException(cpf)
    def buscar(self,cpf):
        funcionario = self.funcionarios.buscar(cpf)
        if(funcionario != None):
            return funcionario
        else:
            raise CpfNaoEncontradoException(cpf)
    def promover(self,cpf):
        funcinario = self.buscar(cpf)
        if(funcinario != None):
            funcinario.is_gerente = True
            funcinario.funcao = "GERENTE"
        else:
            raise CpfNaoEncontradoException(cpf)
    def str(self):
        return self.funcionarios.str()