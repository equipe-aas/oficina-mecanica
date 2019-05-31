from entidades.Pessoa import Pessoa
class Funcionario(Pessoa):
    def __init__(self, rg, cpf, nome, funcao, data_nasc, salario,endereco,telefone):
        Pessoa.__init__(cpf, nome, endereco, telefone)
        self.rg = rg
        self.funcao = funcao
        self.data_nasc = data_nasc
        self.salario = salario
        if(funcao == "GERENTE"):
            self.is_gerente = True
        else:
            self.is_gerente = False

    def __str__(self):
        string = "RG: "+str(self.rg)+"\nCPF: "+str(self.cpf)+"\nNOME: "+self.nome+"\nFUNCAO: "+self.funcao+\
                 "DATA NASCIMENTO: "+str(self.data_nasc)+"SALARIO: R$ "+round(self.salario,2) + "\n"+ self.endereco.str()
        return string