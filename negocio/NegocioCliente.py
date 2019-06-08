from excessoes.CpfJaExisteException import CpfJaExisteException
from excessoes.CpfNaoEncontradoException import CpfNaoEncontradoException
from negocio.entidades.Cliente import Cliente
from validacao.ValidaDados import ValidaDados
from dados.ConexaoDataBase import ConexaoDataBase

class NegocioCliente:
    def __init__(self):
        self.clientes = ConexaoDataBase()
    def adicionar(self, cpf, nome, endereco, telefone):
        if(self.clientes.buscarCliente(cpf) != None):
            raise CpfJaExisteException(cpf)
        if ValidaDados.validaCliente(cpf, nome, endereco, telefone):
            self.clientes.inserirCliente(Cliente(cpf, nome, endereco, telefone))

    def atualizar(self,cliente):
        if(ValidaDados.validaCliente(cliente.cpf, cliente.nome, cliente.endereco, cliente.telefone)):
            self.clientes.atualizarCliente(cliente)

    def remover(self, cpf):
        cliente = self.clientes.buscarCliente(cpf)
        if(cliente != None):
            self.clientes.deletarCliente(cpf)
        else:
            raise CpfNaoEncontradoException(cpf)
    def buscar(self, cpf):
        cliente = self.clientes.buscarCliente(cpf)
        if(cliente != None):
            return cliente
        else:
            raise CpfNaoEncontradoException(cpf)
    def all_clientes(self):
        return self.clientes.todosClientes()
    def __str__(self):
        string = ""
        for c in self.clientes.todosClientes():
            string += c.__str__()
        return string

