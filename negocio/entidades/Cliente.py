class Cliente:
    def __init__(self, cpf, nome, endereco, telefone):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
    def __str__(self):
        string = "CPF: "+str(self.cpf)+"\nNOME: "+self.nome+"\nTELEFONE: "+self.telefone+"\nENDERECO: "+self.endereco+'\n'
        return string