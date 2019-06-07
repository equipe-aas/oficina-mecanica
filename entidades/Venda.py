from datetime import datetime
from entidades.PecaQuantidade import PecaQuantidade


class Venda:
    def __init__(self,codigo,pecas=[]):
        self.codigo = codigo
        self.pecas = pecas
        self.data = datetime.today().strftime('%d/%m/%Y')
        self.total = 0
    def adicionarItem(self,peca,quantidade):
        pecaQuant = PecaQuantidade(peca, quantidade)
        self.pecas.append(pecaQuant)
        self.total += pecaQuant.total()
    def removerItem(self,codigo):
        for i in self.pecas:
            if i.codigo == codigo:
                self.total -= i.total
                self.pecas.remove(i)
                break
    def __str__(self):
        string = ""
        total= 0
        for i in self.pecas:
            string += i.total()
        string += "\nTOTAL: R$ "+str(total)
        return string
