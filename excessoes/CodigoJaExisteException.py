class CodigoJaExisteException(Exception):
    def __init__(self,codigo):
        self.codigo = codigo
    def __str__(self):
        return ("O CODIGO "+str(self.codigo)+" JA ESTA CADASTRADO!!!")
