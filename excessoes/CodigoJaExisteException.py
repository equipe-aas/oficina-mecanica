class CodigoJaExisteException(BaseException):
    def __init__(self,codigo):
        super().__init__()
        self.codigo = codigo
    def __str__(self):
        return ("O CODIGO \""+str(self.codigo)+"\" JA ESTA CADASTRADO!!!")
