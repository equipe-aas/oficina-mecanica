class RgExisteException(Exception):
    def __init__(self, rg):
        self.rg = rg
    def __str__(self):
        return "O RG "+self.rg +"JA ESTA CADASTRADO!!!"