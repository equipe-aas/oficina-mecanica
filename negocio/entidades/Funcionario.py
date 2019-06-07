from negocio.entidades.Pessoa import Pessoa
class Funcionario(Pessoa):
    def __init__(self, matricula, rg, cpf, nome, funcao, data_nasc, salario,endereco,telefone):
        Pessoa.__init__(self,cpf, nome, endereco, telefone)
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
        string = "MATRICULA: "+str(self.matricula)+"\nRG: "+str(self.rg)+"\nCPF: "+str(self.cpf)+"\nNOME: "+self.nome+\
                 "\nFUNCAO: "+self.funcao+"DATA NASCIMENTO: "+str(self.data_nasc)+"SALARIO: R$ "+round(self.salario,2)+\
                 "\n"+self.endereco.str()
        return string