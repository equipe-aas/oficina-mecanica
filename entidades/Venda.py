from datetime import date
from entidades.ItemVenda import ItemVenda


class Venda:
    def __init__(self):
        self.itens = []
        self.data = date.today().strftime('%d/%m/%Y')
    def adicionarItem(self,item,quantidade):
        if(type(item) == "Peca"):
            self.itens.append(ItemVenda(quantidade, item, None))
        else:
            self.itens.append(ItemVenda(quantidade, None, item))
    def removerItem(self,codigo):
        for i in self.itens:
            if i.codigo == codigo:
                self.itens.remove(i)
    def __str__(self):
        string = ""
        for i in self.itens:
            string += i
        return string
