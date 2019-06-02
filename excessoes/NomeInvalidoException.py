class NomeInvalidoException(BaseException):
    def __init__(self,nome):
        self.nome = nome
    def __str__(self):
        return "O NOME \""+self.nome+"\" NÃO É VALIDO!!!"