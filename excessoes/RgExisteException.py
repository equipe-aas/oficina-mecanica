class RgExisteException(BaseException):
    def __init__(self, rg):
        super().__init__()
        self.rg = rg
    def __str__(self):
        return "O RG \""+self.rg +"\" JA ESTA CADASTRADO!!!"