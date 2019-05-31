class TelefoneInvalidoException(Exception):
    def __init__(self,telefone):
        self.telefone = telefone
    def __str__(self):
        return "O TELEFONE "+self.telefone+" NÃO É VALIDO!!!"