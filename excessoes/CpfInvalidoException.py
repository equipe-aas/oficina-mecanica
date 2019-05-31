class CpfInvalidoException(Exception):
    def __init__(self,cpf):
        self.cpf = cpf
    def __str__(self):
        return "O CPF "+self.cpf+" NAO É INVALIDO"