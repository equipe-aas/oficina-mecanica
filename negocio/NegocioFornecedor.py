from dados.RepositorioFornecedor import RepositorioFornecedor
from excessoes.CnpjExisteException import CnpjExisteException
from excessoes.FornecedorNaoExisteException import FornecedorNaoExisteException
from excessoes.NomeInvalidoException import NomeInvalidoException
from excessoes.TelefoneInvalidoException import TelefoneInvalidoException
from excessoes.EmailInvalidoException import EmailInvalidoException
from entidades.Fornecedor import Fornecedor

class NegocioFornecedor:
    def __init__(self):
        self.fornecedores = RepositorioFornecedor()
    def adicionar(self, cnpj, nome, telefone, email, endereco):
        if self.fornecedores.buscar(cnpj) != None:
            raise CnpjExisteException(cnpj)
        if len(nome) < 5:
            raise NomeInvalidoException(nome)
        if len(telefone) < 8:
            raise TelefoneInvalidoException(telefone)
        if not self.isEmail(email):
            raise EmailInvalidoException(email)
        else:
            self.fornecedores.adicionar(Fornecedor(cnpj, nome, telefone, email, endereco))

    def remover(self,cnpj):
        fornecedor = self.fornecedores.buscar(cnpj)
        if(fornecedor != None):
            self.fornecedores.remover(fornecedor)
        else:
            raise FornecedorNaoExisteException(cnpj)
    def buscar(self,cnpj):
        fornecedor = self.fornecedores.buscar(cnpj)
        if(fornecedor != None):
            return fornecedor
        else:
            raise FornecedorNaoExisteException(cnpj)
    def __str__(self):
        return self.fornecedores.__str__()

    def isEmail(self, email):
        if '@' in list(email):
            return True
        else:
            return False