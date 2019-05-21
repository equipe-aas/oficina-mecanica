class CpfJaExisteException(Exception):
    def __init__(self,cpf):
        self.cpf = cpf
    def str(self):
        return "O CPF "+str(self.cpf)+" JA ESTA CADASTRADO!!!"
