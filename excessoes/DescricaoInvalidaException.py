class DescricaoInvalidaException(Exception):
    def __init__(self, descricao):
        self.descricao = descricao
    def __str__(self):
        return "A DESCRICAO "+"\""+str(self.descricao)+"\""+ " É INVALIDA\nMINIMO 5 CARACTERES!!!"