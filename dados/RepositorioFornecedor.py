class RepositorioFornecedor:
    def __init__(self):
        self.fornecedores = []
    def adicionar(self,fornecedor):
        self.fornecedores.append(fornecedor)
    def remover(self,fornecedor):
        self.fornecedores.remove(fornecedor)
    def buscar(self,cnpj):
        fornecedor = None
        for f in self.fornecedores:
            if f.cnpj == cnpj:
                fornecedor = f
                break
        return fornecedor
    def str(self):
        string = ""
        for s in self.servicos:
            string += s.str() + "\n"
        return string
