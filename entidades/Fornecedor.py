class Fornecedor:
    def __init__(self,cnpj, nome, telefone, email, endereco):
        self.cnpj = cnpj
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    def __str__(self):
        string = "CNPJ: "+str(self.cnpj)+"NOME: "+self.nome+"TELEFONE:" +self.telefone+\
                 "\nEMAIL: "+self.email+"\n"+self.endereco.__str__()
        return string