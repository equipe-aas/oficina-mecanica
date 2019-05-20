class Endereco:
    def __init__(self, rua, bairro, cidade, estado,numero):
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.numero = numero
    def str(self):
        string = self.rua + ", " + self.bairro + ", " + self.cidade + ", " + self.estado + ", " + str(self.numero)
        return string

