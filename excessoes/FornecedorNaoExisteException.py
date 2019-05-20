class FornecedorNaoExisteException(Exception):
    def __init__(self,cnpj):
        self.cnpj = cnpj
    def str(self):
        return ("O CNPJ "+(self.cnpj) + " NA POSSUI CADASTRO!!!")