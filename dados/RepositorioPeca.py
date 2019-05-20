class RepositorioPeca:
    def __init__(self):
        self.pecas = []
    def adicionarPeca(self,peca):
        self.pecas.append(peca)
    def removerPeca(self,peca):
        self.pecas.remove(peca)
    def buscarPeca(self,codigo):
        peca = None
        for p in self.pecas:
            if p.codigo == codigo:
                peca = p
                break
        return peca
    def str(self):
        string = ""
        for p in self.pecas:
            string += p.str() + "\n"
        return string
