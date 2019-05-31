from datetime import datetime
from entidades.ItemVenda import ItemVenda


class Venda:
    def __init__(self,codigo):
        self.codigo = codigo
        self.itens = []
        self.data = datetime.today().strftime('%d/%m/%Y')
        self.total = 0
    def adicionarItem(self,item,quantidade):
        if(type(item) == "Peca"):
            self.itens.append(ItemVenda(quantidade, item, None))
        else:
            self.itens.append(ItemVenda(quantidade, None, item))
        self.total += item.preco_venda
    def removerItem(self,codigo):
        for i in self.itens:
            if i.codigo == codigo:
                self.total += i.preco_venda
                self.itens.remove(i)
                break
    def __str__(self):
        string = ""
        for i in self.itens:
            string += i
        return string
