class CnpjExisteException(BaseException):
    def __init__(self,cnpj):
        super().__init__()
        self.cnpj = cnpj
    def __str__(self):
        return ("O CNPJ \""+str(self.cnpj)+ "\" JÁ ESTA CADASTRADO!!!")