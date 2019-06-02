class ValorInvalidoException(BaseException):
    def __init__(self,valor):
        super().__init__()
        self.valor = valor
    def __str__(self):
        return "\""+self.valor+"\" NAO É UM VALOR VÁLIDO!!!"