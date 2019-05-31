from dados.RepositorioPessoa import RepositorioPessoa
from excessoes.CpfJaExisteException import CpfJaExisteException
from excessoes.CpfNaoEncontradoException import CpfNaoEncontradoException
from excessoes.RgExisteException import RgExisteException
from excessoes.NomeInvalidoException import NomeInvalidoException
from excessoes.SenhaInvalidaException import SenhaInvalidaException
from excessoes.ValorInvalidoException import ValorInvalidoException
from excessoes.TelefoneInvalidoException import TelefoneInvalidoException
from excessoes.LoginInvalidoException import LoginInvalidoException
from validacao.ValidaDados import ValidaDados
from entidades.Funcionario import Funcionario

class NegocioFuncionario:
    matricula = 0
    def __init__(self):
        self.funcionarios = RepositorioPessoa()
    def adicionar(self, rg, cpf, nome, funcao, data_nasc, salario,endereco,telefone):
        if self.funcionarios.buscar(cpf) != None:
            raise CpfJaExisteException(cpf)
        if self.buscarPorRg(rg) != None:
            raise RgExisteException(rg)
        if len(nome) < 5:
            raise NomeInvalidoException(nome)
        if(salario < 0):
            raise ValorInvalidoException(salario)
        if(len(telefone) < 8 or not ValidaDados.__isNumeric__(telefone)):
            raise TelefoneInvalidoException(telefone)
        else:
            NegocioFuncionario.matricula += 1
            self.funcionarios.adicionar(Funcionario(NegocioFuncionario.matricula,rg, cpf, nome, funcao,
                                                    data_nasc, salario, endereco, telefone))
    def remover(self,cpf):
        funcionario = self.funcionarios.buscar(cpf)
        if(funcionario != None):
            self.funcionarios.remover(funcionario)
        else:
            raise CpfNaoEncontradoException(cpf)
    def buscar(self,cpf):
        funcionario = self.funcionarios.buscar(cpf)
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
        for i in self.funcionarios.pessoas:
            if i.login == login:
                funcionario = i
                break
        return funcionario
    def buscarPorRg(self,rg):
        funcionario = None
        for i in self.funcionarios.pessoas:
            if i.rg == rg:
                funcionario = i
                break
        return funcionario
    def promover(self,cpf):
        funcinario = self.buscar(cpf)
        if(funcinario != None):
            funcinario.is_gerente = True
            funcinario.funcao = "GERENTE"
        else:
            raise CpfNaoEncontradoException(cpf)
    def __str__(self):
        return self.funcionarios.__str__()