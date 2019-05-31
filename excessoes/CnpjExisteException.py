class CnpjExisteException(Exception):
    def __init__(self,cnpj):
        self.cnpj = cnpj
    def __str__(self):
        return ("O CNPJ: "+str(self.cnpj)+ " JÁ ESTA CADASTRADO!!!")