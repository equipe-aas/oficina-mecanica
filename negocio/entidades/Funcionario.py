class Funcionario:
    def __init__(self, matricula, rg, cpf, nome, funcao, data_nasc, salario, endereco, telefone):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.matricula = matricula
        self.rg = rg
        self.funcao = funcao
        self.data_nasc = data_nasc
        self.salario = salario
        self.login = cpf
        self.senha = rg
        if(funcao == "GERENTE"):
            self.is_gerente = True
        else:
            self.is_gerente = False
    def __str__(self):
        string = "\nMATRICULA: "+str(self.matricula)+"\nRG: "+str(self.rg)+"\nCPF: "+str(self.cpf)+"\nNOME: "+self.nome+\
                 "\nFUNCAO: "+self.funcao+"\nDATA NASCIMENTO: "+str(self.data_nasc)+"\nSALARIO: R$ "+str(round(self.salario,2))+\
                 "\nTELEFONE: "+self.telefone+"\nENDERECO: "+self.endereco
        return string