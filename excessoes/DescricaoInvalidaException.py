class DescricaoInvalidaException(BaseException):
    def __init__(self, descricao):
        super().__init__()
        self.descricao = descricao
    def __str__(self):
        return "A DESCRICAO \""+str(self.descricao)+"\" É INVALIDA\nMINIMO 5 CARACTERES!!!"