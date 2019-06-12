from datetime import date
from negocio.entidades.PecaQuantidade import PecaQuantidade

class PedidoDePeca:
    def __init__(self,fornecedor,pecas = []):
        self.pecas = pecas
        self.fornecedor = fornecedor
        self.data = date.today().strftime('%d/%m/%Y')
    def adicionar(self, peca,quantidade):
        self.pecas.append(PecaQuantidade(peca,quantidade))
    def remover(self,peca):
        self.pecas.remove(peca)
    def __str__(self):
        string  = ""
        for p in self.pecas:
            string += (p.str())
            string += "\n"
        string += "TOTAL: R$ " + str(self.calcularTotal())
        return string
    def calcularTotal(self):
        total = 0.0
        for p in self.pecas:
            total += p.peca.preco_venda
        return round(total,2)