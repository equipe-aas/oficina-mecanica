class ValorInvalidoException(Exception):
    def __init__(self,valor):
        self.valor = valor
    def __str__(self):
        return self.valor+" NAO É UM VALOR VÁLIDO!!!"