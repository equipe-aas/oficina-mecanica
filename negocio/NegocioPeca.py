from excessoes.CodigoNaoEncontradoException import CodigoNaoEncontradoException
from entidades.Peca import Peca
from db.ConexaoDataBase import ConexaoDataBase
from validacao.ValidaDados import ValidaDados

class NegocioPeca:
    def __init__(self):
        self.pecas = ConexaoDataBase()
    def adicionar(self, descricao, fornecedor, preco_custo, preco_venda, quantidade):
        if ValidaDados.validaPeca(descricao,preco_custo, preco_venda, quantidade):
            self.pecas.inserirPeca(Peca(0,descricao, fornecedor, preco_custo, preco_venda, quantidade))

    def atualizar(self,peca):
        if ValidaDados.validaPeca(peca.descricao,peca.preco_custo, peca.preco_venda, peca.quantidade):
            self.pecas.atualizarPeca(peca)

    def remover(self,codigo):
        peca = self.pecas.buscarPeca(codigo)
        if(peca != None):
            self.pecas.deletarPedido(codigo)
        else:
            raise CodigoNaoEncontradoException(codigo)
    def buscar(self, codigo):
        peca = self.pecas.buscarPeca(codigo)
        if (peca != None):
            return peca
        else:
            raise CodigoNaoEncontradoException(codigo)
    def all_pecas(self):
        return self.pecas.todasPecas()
    def __str__(self):
        string = ""
        for i in self.ṕecas.todasPecas():
            string += i.__str__()
        return string