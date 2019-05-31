class SenhaInvalidaException(Exception):
    def __init__(self,senha):
        self.senha = senha
    def __str__(self):
        return "A SENHA "+self.senha+" NÃO É VALIDA!!!"