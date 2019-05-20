from datetime import date
from entidades import Peca
from entidades.ItemVenda import ItemVenda


class Venda:
    def __init__(self):
        self.produtos = []
        self.data = date.today().strftime('%d/%m/%Y')
    def adicionarItem(self,item,quantidade):
        if(type(item) == Peca):
            self.produtos.append(ItemVenda(quantidade, item, None))
        else:
            self.produtos.append(ItemVenda(quantidade, None, item))