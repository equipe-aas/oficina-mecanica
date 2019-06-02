from negocio.NegocioCliente import NegocioCliente
from negocio.NegocioFornecedor import NegocioFornecedor
from negocio.NegocioFuncionario import NegocioFuncionario
from negocio.NegocioPeca import NegocioPeca
from negocio.NegocioPedido import NegocioPedido
from negocio.NegocioServico import NegocioServico
from negocio.NegocioVenda import NegocioVenda

class Fachada:
    def __init__(self):
        self.clientes = NegocioCliente()
        self.fornecedores = NegocioFornecedor()
        self.funcionarios = NegocioFuncionario()
        self.pecas = NegocioPeca()
        self.pedidos = NegocioPedido()
        self.servicos = NegocioServico()
        self.vendas = NegocioVenda()
    def adicionarCliente(self, cpf, nome, endereco, telefone):
        self.clientes.adicionar(cpf, nome, endereco, telefone)
    def removerCliente(self, cpf):
        self.clientes.remover(cpf)
    def buscarCliente(self, cpf):
        return self.clientes.buscar(cpf)
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

    def adicionarPeca(self, descricao, fornecedor, preco_custo, preco_venda, quantidade):
        self.pecas.adicionar( descricao, fornecedor, preco_custo, preco_venda, quantidade)
    def removerPeca(self,codigo):
        self.pecas.remover(codigo)
    def buscarPeca(self,codigo):
        return self.pecas.buscar(codigo)
    def __str__peca(self):
        return self.pecas.__str__()

    def adicionarPedido(self,pedido):
        self.pedidos.adicionar(pedido)
    def removerPedido(self,codigo):
        self.pedidos.remover(codigo)
    def buscarPedido(self,codigo):
        return self.pedidos.buscar(codigo)
    def __str__pedido(self,codigo):
        return self.pedidos.__str__()

    def adicionarServico(self, descricao, preco_venda, peca):
        self.servicos.adicionar(descricao, preco_venda, peca)
    def removerServico(self,codigo):
        self.servicos.remover(codigo)
    def buscarServico(self,codigo):
        return self.servicos.buscar(codigo)
    def __str__servico(self):
        return self.servicos.__str__()

    def adicionarVenda(self,venda):
        self.vendas.adicionar(venda)
    def removerVenda(self,codigo):
        self.vendas.remover(codigo)
    def __str__venda(self):
        return self.vendas.__str__()

    def login(self,log,senha):
        return self.funcionarios.login(log,senha)
