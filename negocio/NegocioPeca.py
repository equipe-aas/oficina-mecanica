from dados.RepositorioPeca import RepositorioPeca
from excessoes.CodigoJaExisteException import CodigoJaExisteException
from excessoes.CodigoNaoEncontradoException import CodigoNaoEncontradoException

class NegocioPeca:
    def __init__(self):
        self.pecas = RepositorioPeca()
    def adicionar(self,peca):
        if(self.pecas.buscar(peca.codigo) == None):
            self.pecas.adicionar(peca)
        else:
            raise CodigoJaExisteException(peca.codigo)
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