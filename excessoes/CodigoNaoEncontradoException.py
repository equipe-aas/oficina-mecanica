class CodigoNaoEncontradoException(Exception):
    def __init__(self,codigo):
        self.codigo = codigo
    def str(self):
        return ("O CODIGO "+str(self.codigo)+" NAO POSSUI CADASTRO!!!")