from dados.ConexaoDataBase import ConexaoDataBase
from excessoes.CodigoNaoEncontradoException import CodigoNaoEncontradoException
from excessoes.CpfJaExisteException import CpfJaExisteException
from excessoes.CpfNaoEncontradoException import CpfNaoEncontradoException
from excessoes.RgExisteException import RgExisteException
from excessoes.SenhaInvalidaException import SenhaInvalidaException
from excessoes.LoginInvalidoException import LoginInvalidoException
from validacao.ValidaDados import ValidaDados
from negocio.entidades.Funcionario import Funcionario

class NegocioFuncionario:
    def __init__(self):
        self.funcionarios = ConexaoDataBase()
    def adicionar(self, rg, cpf, nome, funcao, data_nasc, salario,endereco,telefone):
        if self.funcionarios.buscar(cpf) != None:
            raise CpfJaExisteException(cpf)
        if self.buscarPorRg(rg) != None:
            raise RgExisteException(rg)
        if ValidaDados.validaFuncionario(rg, cpf, nome,data_nasc, salario,endereco,telefone):
            self.funcionarios.inserirFuncionario(Funcionario(0,rg, cpf, nome, funcao,data_nasc, salario, endereco, telefone))

    def atualizar(self,funcinario):
        if ValidaDados.validaFuncionario(funcinario.rg, funcinario.cpf, funcinario.nome, funcinario.data_nasc,\
                                         funcinario.salario, funcinario.endereco,funcinario.telefone):
            self.funcionarios.atualizarFuncionario(funcinario)

    def remover(self,cpf):
        funcionario = self.funcionarios.buscarFuncionario(cpf)
        if(funcionario != None):
            self.funcionarios.deletarFuncionario(funcionario)
        else:
            raise CpfNaoEncontradoException(cpf)

    def buscar(self,cpf):
        funcionario = self.funcionarios.buscarFuncionario(cpf)
        if(funcionario != None):
            return funcionario
        else:
            raise CpfNaoEncontradoException(cpf)

    def login(self,log,senha):
        funcionario = self.buscarPorLogin(log)
        if funcionario == None:
            raise LoginInvalidoException(log)
        if funcionario.senha == senha:
            return True
        else:
            raise SenhaInvalidaException(senha)
    def buscarPorLogin(self,login):
        funcionario = None
        for i in self.funcionarios.todosFuncionarios():
            if i.login == login:
                funcionario = i
                break
        return funcionario
    def buscarPorRg(self,rg):
        funcionario = None
        for i in self.funcionarios.todosFuncionarios():
            if i.rg == rg:
                funcionario = i
                break
        return funcionario
    def rebaixar(self,matricula):
        funcinario = self.funcionarios.buscarFuncionario(matricula)
        if (funcinario != None):
            funcinario.is_gerente = False
            funcinario.funcao = "Funcionario"
            self.atualizar(funcinario)
        else:
            raise CodigoNaoEncontradoException(matricula)

    def promover(self,matricula):
        funcinario = self.funcionarios.buscarFuncionario(matricula)
        if(funcinario != None):
            funcinario.is_gerente = True
            funcinario.funcao = "GERENTE"
            self.atualizar(funcinario)
        else:
            raise CodigoNaoEncontradoException(matricula)
    def all_funcionarios(self):
        return self.funcionarios.todosFuncionarios()
    def __str__(self):
        string = ""
        for i in self.funcionarios.todosFuncionarios():
            string += i.__str__()
        return string