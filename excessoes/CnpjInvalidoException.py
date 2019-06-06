class CnpjInvalidoException(BaseException):
    def __init__(self,cnpj):
        self.cnpj = cnpj
    def __str__(self):
        return 'O CNPJ \"'+self.cnpj+"\" NÃO E VALIDO!!!"
