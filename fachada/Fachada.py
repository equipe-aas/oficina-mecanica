from negocio.NegocioCliente import NegocioCliente
from negocio.NegocioFornecedor import NegocioFornecedor
from negocio.NegocioFuncionario import NegocioFuncionario
from negocio.NegocioPeca import NegocioPeca
from negocio.NegocioPedido import NegocioPedido
from negocio.NegocioServico import NegocioServico
from negocio.NegocioVenda import NegocioVenda

class Fachada:
    fachada = None
    def __init__(self):
        self.clientes = NegocioCliente()
        self.fornecedores = NegocioFornecedor()
        self.funcionarios = NegocioFuncionario()
        self.pecas = NegocioPeca()
        self.pedidos = NegocioPedido()
        self.servicos = NegocioServico()
        self.vendas = NegocioVenda()
    @staticmethod
    def getInstance(self):
        if Fachada.fachada == None:
            Fachada.fachada = Fachada()
        return Fachada.fachada

    def adicionarCliente(self, cpf, nome, endereco, telefone):
        self.clientes.adicionar(self, cpf, nome, endereco, telefone)
    def removerCliente(self, cpf):
        self.clientes.remover(cpf)
    def buscarCliente(self, cpf):
        return self.clientes.buscar(self, cpf)
    def __str__cliente(self):
        return self.clientes.__str__()

    def adicionarFornecedor(self, cnpj, nome, telefone, email, endereco):
        self.fornecedores.adicionar(cnpj, nome, telefone, email, endereco)
    def removerFornecedor(self,cnpj):
        self.fornecedores.remover(cnpj)
    def buscarFornecedor(self, cnpj):
        return self.fornecedores.buscar(cnpj)
    def __str__fornecedor(self):
        return self.fornecedores.__str__()

    def adicionarFuncionario(self, rg, cpf, nome, funcao, data_nasc, salario, endereco, telefone):
        self.funcionarios.adicionar(rg, cpf, nome, funcao, data_nasc, salario,endereco,telefone)
    def removerFuncionario(self, cpf):
        self.funcionarios.remover(cpf)
    def buscarFuncionarioCpf(self,cpf):
        return self.funcionarios.buscar(cpf)
    def buscarFuncionarioRg(self, rg):
        return self.funcionarios.buscarPorRg(rg)
    def promoverFuncionario(self, cpf):
        self.funcionarios.promover(cpf)
    def __str__funcionario(self):
        return self.funcionarios.__str__()