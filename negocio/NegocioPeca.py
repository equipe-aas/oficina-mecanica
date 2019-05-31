from dados.RepositorioPeca import RepositorioPeca
from excessoes.CodigoNaoEncontradoException import CodigoNaoEncontradoException
from excessoes.DescricaoInvalidaException import DescricaoInvalidaException
from excessoes.ValorInvalidoException import ValorInvalidoException
from entidades.Peca import Peca

class NegocioPeca:
    codigo = 0
    def __init__(self):
        self.pecas = RepositorioPeca()
    def adicionar(self, descricao, fornecedor, preco_custo, preco_venda, quantidade):
        if len(descricao)<5 :
            raise DescricaoInvalidaException(descricao)
        if preco_custo < 0:
            raise ValorInvalidoException(preco_custo)
        if preco_venda < 0:
            raise ValorInvalidoException(preco_venda)
        if quantidade < 0:
            raise ValorInvalidoException(quantidade)
        else:
            NegocioPeca.codigo += 1
            self.pecas.adicionar(Peca(NegocioPeca.codigo,descricao, fornecedor, preco_custo, preco_venda, quantidade))
    def remover(self,codigo):
        peca = self.pecas.buscar(codigo)
        if(peca != None):
            self.pecas.remover(peca)
        else:
            raise CodigoNaoEncontradoException(codigo)
    def buscar(self, codigo):
        peca = self.pecas.buscar(codigo)
        if (peca != None):
            return peca
        else:
            raise CodigoNaoEncontradoException(codigo)

    def __str__(self):
        return self.pecas.__str__()