class CpfJaExisteException(Exception):
    def __init__(self,cpf):
        self.cpf = cpf
    def __str__(self):
        return "O CPF "+str(self.cpf)+" JA ESTA CADASTRADO!!!"
