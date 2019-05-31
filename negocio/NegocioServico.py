from dados.RepositorioServico import RepositorioServico
from excessoes.DescricaoInvalidaException import DescricaoInvalidaException
from excessoes.ValorInvalidoException import ValorInvalidoException
from entidades.Servico import Servico
from excessoes.CodigoNaoEncontradoException import CodigoNaoEncontradoException

class NegocioServico:
    codigo = 0
    def __init__(self):
        self.servicos = RepositorioServico()
    def adicionar(self, descricao, preco_venda, peca = None):
        if(len(descricao) < 5):
            raise DescricaoInvalidaException(descricao)
        if(preco_venda < 0):
            raise ValorInvalidoException(preco_venda)
        else:
            NegocioServico.codigo += 1
            self.servicos.adicionar(Servico( NegocioServico.codigo, descricao, preco_venda, peca))

    def remover(self,codigo):
        self.servicos.remover(self.buscar(codigo))

    def buscar(self,codigo):
        servico = self.servicos.buscar(codigo)
        if servico == None:
            raise CodigoNaoEncontradoException(codigo)
        else:
            return servico
    def __str__(self):
        return self.servicos.__str__()
