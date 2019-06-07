from entidades.Servico import Servico
from excessoes.CodigoNaoEncontradoException import CodigoNaoEncontradoException
from db.ConexaoDataBase import ConexaoDataBase
from validacao.ValidaDados import ValidaDados

class NegocioServico:
    codigo = 0
    def __init__(self):
        self.servicos = ConexaoDataBase()
    def adicionar(self, descricao, preco_venda, peca = None):
        if ValidaDados.validaServico(descricao,preco_venda):
            self.servicos.inserirServico(Servico(NegocioServico.codigo, descricao, preco_venda, peca))
        
    def remover(self,codigo):
        self.servicos.deletarServico(codigo)

    def buscar(self,codigo):
        servico = self.servicos.buscarServico(codigo)
        if servico == None:
            raise CodigoNaoEncontradoException(codigo)
        else:
            return servico
    def __str__(self):
        string = ""
        for i in self.servicos.todosServicos():
            string += i.__str__()
        return string
