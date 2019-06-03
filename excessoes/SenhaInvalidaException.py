class SenhaInvalidaException(BaseException):
    def __init__(self,senha):
        super().__init__()
        self.senha = senha
    def __str__(self):
        return "A SENHA \""+self.senha+"\" NÃO É VALIDA!!!"