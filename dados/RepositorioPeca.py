class RepositorioPeca:
    def __init__(self):
        self.pecas = []
    def adicionar(self,peca):
        self.pecas.append(peca)
    def remover(self,peca):
        self.pecas.remove(peca)
    def buscar(self,codigo):
        peca = None
        for p in self.pecas:
            if p.codigo == codigo:
                peca = p
                break
        return peca
    def __str__(self):
        string = ""
        for p in self.pecas:
            string += p.str() + "\n"
        return string
