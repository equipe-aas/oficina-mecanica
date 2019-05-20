class RepositorioServico:
    def __init__(self):
        self.servicos = []
    def adicionar(self,servico):
        self.servicos.append(servico)
    def remover(self,servico):
        self.pecas.remove(servico)
    def buscar(self,codigo):
        servico = None
        for s in self.servicos:
            if s.codigo == codigo:
                servico = s
                break
        return servico
    def str(self):
        string = ""
        for s in self.servicos:
            string += s.str() + "\n"
        return string
