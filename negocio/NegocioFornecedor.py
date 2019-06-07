from excessoes.CnpjExisteException import CnpjExisteException
from excessoes.FornecedorNaoExisteException import FornecedorNaoExisteException
from entidades.Fornecedor import Fornecedor
from validacao.ValidaDados import ValidaDados
from db.ConexaoDataBase import ConexaoDataBase

class NegocioFornecedor:
    def __init__(self):
        self.fornecedores = ConexaoDataBase()
    def adicionar(self, cnpj, nome, telefone, email, endereco):
        fornecedor = Fornecedor(cnpj, nome, telefone, email, endereco)
        if self.fornecedores.buscarFornecedor(cnpj) != None:
            raise CnpjExisteException(cnpj)
        if ValidaDados.validaFornecedor(cnpj, nome, telefone, email, endereco):
            self.fornecedores.inserirFornecedor(fornecedor)

    def remover(self,cnpj):
        fornecedor = self.fornecedores.buscarFornecedor(cnpj)
        if(fornecedor != None):
            self.fornecedores.deletarFornecedor(cnpj)
        else:
            raise FornecedorNaoExisteException(cnpj)

    def atualizar(self,fornecedor):
        if ValidaDados.validaFornecedor(fornecedor.cnpj, fornecedor.nome, fornecedor.telefone, fornecedor.email, fornecedor.endereco):
            self.fornecedores.atualizarFornecedor(fornecedor)

    def buscar(self,cnpj):
        fornecedor = self.fornecedores.buscarFornecedor(cnpj)
        if fornecedor != None:
            return fornecedor
        else:
            raise FornecedorNaoExisteException(cnpj)
    def all_fornecedores(self):
        return self.fornecedores.todosFornecedores()
    def __str__(self):
        string = ""
        for f in self.fornecedores.todosFornecedores():
            string += f.__str__()
        return string