class CpfNaoEncontradoException(Exception):
    def __init__(self,cpf):
        self.cpf = cpf
    def str(self):
        return "O CPF "+str(self.cpf)+" NAO ESTA CADASTRADO!!!"