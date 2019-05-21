class CodigoJaExisteException(Exception):
    def __init__(self,codigo):
        self.codigo = codigo
    def str(self):
        return ("O CODIGO "+str(self.codigo)+" JA ESTA CADASTRADO!!!")
