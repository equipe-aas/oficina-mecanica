class CnpjExisteException(Exception):
    def __init__(self,cnpj):
        self.cnpj = cnpj
    def str(self):
        return ("O CNPJ: "+str(self.cnpj)+ " JÁ ESTA CADASTRADO!!!")