class CodigoNaoEncontradoException(Exception):
    def __init__(self,codigo):
        self.codigo = codigo
    def __str__(self):
        return ("O CODIGO "+str(self.codigo)+" NAO POSSUI CADASTRO!!!")