class Fornecedor:
    def __init__(self,cnpj, nome, email, endereco):
        self.cnpj = cnpj
        self.nome = nome
        self.email = email
        self.endereco = endereco
    def __str__(self):
        string = "CNPJ: "+str(self.cnpj)+"NOME: "+self.nome+"\nEMAIL: "+self.email+"\n"+self.endereco.str()
        return string