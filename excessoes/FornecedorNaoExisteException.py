class FornecedorNaoExisteException(Exception):
    def __init__(self,cnpj):
        self.cnpj = cnpj
    def __str__(self):
        return ("O CNPJ "+(self.cnpj) + " NA POSSUI CADASTRO!!!")