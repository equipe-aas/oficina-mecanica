class TelefoneInvalidoException(BaseException):
    def __init__(self,telefone):
        super().__init__()
        self.telefone = telefone
    def __str__(self):
        return "O TELEFONE \""+self.telefone+"\" NÃO É VALIDO!!!"