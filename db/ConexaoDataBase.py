import sqlite3
from entidades.Cliente import Cliente
from entidades.Fornecedor import Fornecedor
from entidades.Funcionario import Funcionario
from entidades.Peca import Peca
from entidades.PedidoDePeca import PedidoDePeca
from entidades.Servico import Servico


class ConexaoDataBase:
    def __init__(self):
        self.conexao = sqlite3.connect('database.sqlite')
        self.cursor = self.conexao.cursor()
    #################################### CRUD CLIENTES ######################################################
    def inserirCliente(self,cliente):
        self.cursor.execute('INSERT INTO clientes(cpf, nome, endereco, telefone) VALUES(?,?,?,?)',
                            (cliente.cpf,cliente.nome,cliente.endereco,cliente.telefone))
        self.conexao.commit()

    def buscarCliente(self,cpf):
        comando = 'SELECT * FROM clientes WHERE cpf = ?'
        c = self.cursor.execute(comando,(cpf,)).fetchall()
        return Cliente(c[0][0],c[0][1],c[0][2],c[0][3])

    def atualizarCliente(self,cliente):
        self.cursor.execute('UPDATE clientes SET nome = ?,endereco = ?, telefone = ? WHERE cpf = ?',\
                              (cliente.nome,cliente.endereco,cliente.telefone,cliente.cpf))

        self.conexao.commit()

    def deletarCliente(self,cpf):
        comando = 'DELETE FROM clientes WHERE cpf = ?'

        self.cursor.execute(comando,(cpf,))
        self.conexao.commit()

    def todosClientes(self):
        comando = 'SELECT * FROM clientes'
        self.cursor.execute(comando)
        clientes = []
        for c in self.cursor.fetchall():
            clientes.append(Cliente(c[0],c[1],c[2],c[3]))
        return clientes
    #################################### CRUD FORNECEDORES ######################################################
    def inserirFornecedor(self,fornecedor):
        self.cursor.execute('INSERT INTO fornecedores(cnpj, nome, telefone, email, endereco) VALUES(?,?,?,?,?)',
                            (fornecedor.cnpj, fornecedor.nome, fornecedor.telefone,fornecedor.email,fornecedor.endereco))
        self.conexao.commit()

    def buscarFornecedor(self,cnpj):
        comando = 'SELECT * FROM fornecedores WHERE cnpj = ?'
        c = self.cursor.execute(comando,(cnpj,)).fetchall()
        return Fornecedor(c[0][0],c[0][1],c[0][2],c[0][3],c[0][4])

    def atualizarFornecedor(self,fornecedor):
        self.cursor.execute('UPDATE fornecedores SET nome = ?, telefone = ?, email = ?, endereco = ?, telefone = ? WHERE cnpj = ?',\
                              (fornecedor.nome, fornecedor.telefone,fornecedor.email,fornecedor.endereco,fornecedor.cnpj))

        self.conexao.commit()

    def deletarFornecedor(self,cnpj):
        comando = 'DELETE FROM fornecedores WHERE cnpj = ?'

        self.cursor.execute(comando,(cnpj,))
        self.conexao.commit()

    def todosFornecedores(self):
        comando = 'SELECT * FROM fornecedores'
        self.cursor.execute(comando)
        fornecedores = []
        for f in self.cursor.fetchall():
            fornecedores.append(Fornecedor(f[0],f[1],f[2],f[3],f[4]))
        return fornecedores
    #################################### CRUD FUNCIONARIOS ######################################################
    def inserirFuncionario(self, func):
        self.cursor.execute('INSERT INTO funcionarios(rg, cpf, nome, funcao, dataNascimento, salario,endereco,telefone) VALUES(?,?,?,?,?,?,?,?)',
                            (func.rg, func.cpf, func.nome, func.funcao, func.data_nasc, func.salario, func.endereco, func.telefone))
        self.conexao.commit()

    def buscarFuncionario(self, matricula):
        comando = 'SELECT * FROM funcionarios WHERE matricula = ?'
        c = self.cursor.execute(comando, (matricula,)).fetchall()
        return Funcionario(c[0][0], c[0][1], c[0][2], c[0][3], c[0][4], c[0][5], c[0][6], c[0][7])

    def atualizarFuncionario(self, func):
        self.cursor.execute(
            'UPDATE funcionarios SET rg = ?, cpf = ?, nome = ?, funcao = ?, dataNascimento = ?, salario = ?,\
             endereco = ?, telefone = ? WHERE matricula = ?',\
            (func.rg, func.cpf, func.nome, func.funcao, func.data_nasc, func.salario, func.endereco, func.telefone,func.matricula))

        self.conexao.commit()

    def deletarFuncionario(self, matricula):
        comando = 'DELETE FROM funcionarios WHERE matricula = ?'

        self.cursor.execute(comando, (matricula,))
        self.conexao.commit()

    def todosFuncionarios(self):
        comando = 'SELECT * FROM funcionarios'
        self.cursor.execute(comando)
        funcionarios = []
        for f in self.cursor.fetchall():
            funcionarios.append(Fornecedor(f[0], f[1], f[2], f[3], f[4],f[5],f[6],f[7]))
        return funcionarios
    #################################### CRUD PECAS ######################################################
    def inserirPeca(self, peca):
        self.cursor.execute(
            'INSERT INTO pecas(descricao, fornecedor_cnpj, preco_custo, preco_venda, quantidade) VALUES(?,?,?,?,?)',
            (peca.descricao, peca.fornecedor, peca.preco_custo, peca.preco_venda, peca.quantidade))
        self.conexao.commit()

    def buscarPeca(self, codigo):
        comando = 'SELECT * FROM pecas WHERE codigo = ?'
        c = self.cursor.execute(comando, (codigo,)).fetchall()
        return Peca(c[0][0], c[0][1], c[0][2], c[0][3], c[0][4], c[0][5])

    def atualizarPeca(self, peca):
        self.cursor.execute(
            'UPDATE pecas SET descricao = ?, fornecedor_cnpj = ?, preco_custo = ?, preco_venda = ?, quantidade = ? WHERE codigo = ?', \
            (peca.descricao, peca.fornecedor, peca.preco_custo, peca.preco_venda, peca.quantidade,peca.codigo))
        self.conexao.commit()

    def deletarPeca(self, codigo):
        comando = 'DELETE FROM pecas WHERE codigo = ?'

        self.cursor.execute(comando, (codigo,))
        self.conexao.commit()

    def todosPecas(self):
        comando = 'SELECT * FROM pecas'
        self.cursor.execute(comando)
        pecas = []
        for p in self.cursor.fetchall():
            pecas.append(Peca(p[0], p[1], p[2], p[3], p[4], p[5]))
        return pecas

    #################################### CRUD PEDIDO ######################################################
    def inserirPedido(self, pedido):
        self.cursor.execute(
            'INSERT INTO pedidos(fornecedor_cnpj, data) VALUES(?,?)',
            (pedido.fornecedor, pedido.data))
        self.conexao.commit()

        ped = self.cursor.execute('SELECT MAX(codigo) FROM pedidos')

        for p in pedido.pecas:
            self.cursor.execute(
                'INSERT INTO pedido_peca(pedido_codigo,peca_codigo,quantidade) VALUES(?,?,?)',
                (ped[0][0], p.codigo, p.quantidade))

    def buscarPedido(self, codigo):
        comando = 'SELECT * FROM pedidos WHERE codigo = ?'
        pedido = self.cursor.execute(comando, (codigo,)).fetchall()

    #################################### CRUD SERVICO ######################################################

    def inserirServico(self, servico):
        self.cursor.execute(
            'INSERT INTO servicos(descricao, servico_codigo, preco_venda) VALUES(?,?,?)',
            (servico.descricao, servico.codigo, servico.preco_venda))
        self.conexao.commit()

    def buscarServico(self, codigo):
        comando = 'SELECT * FROM servicos WHERE codigo = ?'
        c = self.cursor.execute(comando, (codigo,)).fetchall()
        return Servico(c[0][0], c[0][1], c[0][2], c[0][3])

    def atualizarServico(self, servico):
        self.cursor.execute(
            'UPDATE servicos SET descricao = ?, servico_codigo = ?, preco_venda = ? WHERE codigo = ?', \
            (servico.descricao, servico.codigo, servico.preco_venda, servico.codigo))
        self.conexao.commit()

    def deletarServico(self, codigo):
        comando = 'DELETE FROM servicos WHERE codigo = ?'

        self.cursor.execute(comando, (codigo,))
        self.conexao.commit()

    def todosServico(self):
        comando = 'SELECT * FROM servicos'
        self.cursor.execute(comando)
        servicos = []
        for p in self.cursor.fetchall():
            servicos.append(Servico(p[0], p[1], p[2], p[3]))
        return servicos