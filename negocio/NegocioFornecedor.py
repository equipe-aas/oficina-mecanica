from dados.RepositorioFornecedor import RepositorioFornecedor
from excessoes.CnpjExisteException import CnpjExisteException
from excessoes.FornecedorNaoExisteException import FornecedorNaoExisteException

class NegocioFornecedor:
    def __init__(self):
        self.fornecedores = RepositorioFornecedor()
    def adicionar(self,fornecedor):
        if(self.fornecedores.buscar(fornecedor.cnpj) == None):
            self.fornecedores.adicionar(fornecedor)
        else:
          raise CnpjExisteException()
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
    def str(self):
        return self.fornecedores.str()