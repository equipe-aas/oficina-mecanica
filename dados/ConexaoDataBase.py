import sqlite3
from negocio.entidades.PecaQuantidade import PecaQuantidade
from negocio.entidades.Cliente import Cliente
from negocio.entidades.Fornecedor import Fornecedor
from negocio.entidades.Funcionario import Funcionario
from negocio.entidades.Peca import Peca
from negocio.entidades.PedidoDePeca import PedidoDePeca
from negocio.entidades.Servico import Servico
from negocio.entidades.Venda import Venda


class ConexaoDataBase:
    def __init__(self):
        self.conexao = sqlite3.connect('/home/saucesar/PycharmProjects/oficina-mecanica/db/database.sqlite')
        self.cursor = self.conexao.cursor()
    #################################### CRUD CLIENTES ######################################################
    def inserirCliente(self,cliente):
        self.cursor.execute('INSERT INTO clientes(cpf, nome, endereco, telefone) VALUES(?,?,?,?)',
                            (cliente.cpf,cliente.nome,cliente.endereco,cliente.telefone))
        self.conexao.commit()

    def buscarCliente(self,cpf):
        comando = 'SELECT * FROM clientes WHERE cpf = ?'
        c = self.cursor.execute(comando,(cpf,)).fetchall()
        if(len(c) < 1):
            cliente = None
        else:
            cliente = Cliente(c[0][0],c[0][1],c[0][2],c[0][3])
        return cliente

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

        if(len(c) < 1):
            fornecedor = None
        else:
            fornecedor = Fornecedor(c[0][0], c[0][1], c[0][2], c[0][3], c[0][4])
        return fornecedor

    def atualizarFornecedor(self,fornecedor):
        comando = 'UPDATE fornecedores SET nome = ?, telefone = ?, email = ?, endereco = ? WHERE cnpj = ?'
        self.cursor.execute(comando,(fornecedor.nome, fornecedor.telefone,fornecedor.email,fornecedor.endereco,fornecedor.cnpj))

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
        comando = 'INSERT INTO funcionarios(rg, cpf, nome, funcao, dataNascimento, salario,endereco,telefone,login,senha)\
                   VALUES(?,?,?,?,?,?,?,?,?,?)'
        self.cursor.execute(comando,(func.rg, func.cpf, func.nome, func.funcao, func.data_nasc, func.salario,\
                                     func.endereco, func.telefone,func.login,func.senha,))
        self.conexao.commit()

    def buscarFuncionario(self, matricula):
        comando = 'SELECT * FROM funcionarios WHERE matricula = ?'
        c = self.cursor.execute(comando, (matricula,)).fetchall()
        if len(c) < 1:
            funcionario = None
        else:
            funcionario = Funcionario(c[0][0], c[0][1], c[0][2], c[0][3], c[0][4], c[0][5], c[0][6], c[0][7],c[0][8])
            funcionario.login = c[0][9]
            funcionario.senha = c[0][10]
        return funcionario

    def atualizarFuncionario(self, func):
        comando = 'UPDATE funcionarios SET rg = ?, cpf = ?, nome = ?, funcao = ?, dataNascimento = ?, salario = ?,\
                   endereco = ?, telefone = ?, login = ?, senha = ? WHERE matricula = ?'

        self.cursor.execute(comando,(func.rg, func.cpf, func.nome, func.funcao, func.data_nasc, func.salario,\
                            func.endereco, func.telefone, func.login, func.senha, func.matricula))

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
            func = Funcionario(f[0], f[1], f[2], f[3], f[4],f[5],f[6],f[7],f[8])
            func.login = f[9]
            func.senha = f[10]
            funcionarios.append(func)
        return funcionarios
    #################################### CRUD PECAS ######################################################
    def inserirPeca(self, peca):
        self.cursor.execute(
            'INSERT INTO pecas(descricao, fornecedor_cnpj, preco_custo, preco_venda, quantidade) VALUES(?,?,?,?,?)',
            (peca.descricao, peca.fornecedor.cnpj, peca.preco_custo, peca.preco_venda, peca.quantidade))
        self.conexao.commit()

    def buscarPeca(self, codigo):
        comando = 'SELECT * FROM pecas WHERE codigo = ?'
        c = self.cursor.execute(comando, (codigo,)).fetchall()
        if len(c) < 1:
            return None
        return Peca(c[0][0], c[0][1], self.buscarFornecedor(c[0][2]), c[0][3], c[0][4], c[0][5])

    def atualizarPeca(self, peca):
        self.cursor.execute(
            'UPDATE pecas SET descricao = ?, fornecedor_cnpj = ?, preco_custo = ?, preco_venda = ?, quantidade = ? WHERE codigo = ?', \
            (peca.descricao, peca.fornecedor, peca.preco_custo, peca.preco_venda, peca.quantidade,peca.codigo))
        self.conexao.commit()

    def deletarPeca(self, codigo):
        comando = 'DELETE FROM pecas WHERE codigo = ?'

        self.cursor.execute(comando, (codigo,))
        self.conexao.commit()

    def todasPecas(self):
        comando = 'SELECT * FROM pecas'
        self.cursor.execute(comando)
        pecas = []
        for p in self.cursor.fetchall():
            pecas.append(Peca(p[0], p[1], self.buscarFornecedor(p[2]), p[3], p[4], p[5]))
        return pecas
    #################################### CRUD PEDIDO ######################################################
    def inserirPedido(self, pedido):
        self.cursor.execute(
            'INSERT INTO pedidos(fornecedor_cnpj, data) VALUES(?,?)',
            (pedido.fornecedor.cnpj, pedido.data))
        self.conexao.commit()

        ped = self.cursor.execute('SELECT MAX(codigo) FROM pedidos')

        for p in pedido.pecas:
            self.cursor.execute(
                'INSERT INTO pedido_peca(pedido_codigo,peca_codigo,quantidade) VALUES(?,?,?)',
                (ped[0][0], p.codigo, p.quantidade))

        self.conexao.commit()

    def buscarPedido(self, codigo):
        comando = 'SELECT * FROM pedidos WHERE codigo = ?'
        ped = self.cursor.execute(comando, (codigo,)).fetchall()

        if len(ped) < 1:
            return None

        comando = 'SELECT * FROM pedido_peca WHERE pedido_codigo = ?'
        pedido_peca = self.cursor.execute(comando, (codigo,)).fetchall()

        pecas = []
        for p in pedido_peca:
            pecas.append(PecaQuantidade(self.buscarPeca(p[1]),p[2]))

        fornecedor = self.buscarFornecedor(ped[0][1])
        pedido = PedidoDePeca(fornecedor,pecas)
        pedido.data = ped[0][2]
        return pedido

    def atualizarPedido(self, pedido):
        self.deletarPedido(pedido.codigo)
        self.inserirPedido(pedido)

    def deletarPedido(self,codigo):
        pedido = self.buscarPedido(codigo)

        comando = 'DELETE FROM pedido_peca WHERE pedido_codigo = ? AND peca_codigo'

        for p in pedido.pecas:
            self.cursor.execute(comando,(codigo,p.peca.codigo,))

        comando = 'DELETE FROM pedidos WHERE codigo = ?'
        self.cursor.execute(comando, (codigo,))

        self.conexao.commit()

    def todosPedidos(self):
        comando = 'SELECT * FROM pedido_peca'
        self.cursor.execute(comando)
        pedidos = []
        for p in self.cursor.fetchall():
            pedidos.append(self.buscarPedido(p[0]))
        return pedidos
    #################################### CRUD SERVICOS #####################################################
    def inserirServico(self, servico):
        if(servico.peca != None):
            self.cursor.execute(
                'INSERT INTO servicos(descricao, preco_venda, peca_id) VALUES(?,?,?)',
                (servico.descricao, servico.preco_venda, servico.peca.codigo))
        else:
            self.cursor.execute(
                'INSERT INTO servicos(descricao, preco_venda, peca_id) VALUES(?,?,?)',
                (servico.descricao, servico.preco_venda, None))
        self.conexao.commit()

    def buscarServico(self, codigo):
        comando = 'SELECT * FROM servicos WHERE codigo = ?'
        serv = self.cursor.execute(comando, (codigo,)).fetchall()
        if len(serv) < 1:
            return None
        if(serv[0][3] != None):
            servico = Servico(serv[0][0], serv[0][1], serv[0][2], self.buscarPeca(serv[0][3]))
        else:
            servico = Servico(serv[0][0], serv[0][1], serv[0][2], None)

        return servico

    def atualizarServico(self, servico):
        if(servico.peca != None):
            self.cursor.execute(
                'UPDATE servicos SET descricao = ?, preco_venda = ?, peca_id = ? WHERE codigo = ?', \
                (servico.descricao, servico.preco_venda, servico.peca.codigo,servico.codigo))
        else:
            self.cursor.execute(
                'UPDATE servicos SET descricao = ?, preco_venda = ?, peca_id = ? WHERE codigo = ?', \
                (servico.descricao, servico.preco_venda, None, servico.codigo))

        self.conexao.commit()

    def deletarServico(self,codigo):
        comando = 'DELETE FROM servicos WHERE codigo = ?'
        self.cursor.execute(comando, (codigo,))

        self.conexao.commit()

    def todosServicos(self):
        comando = 'SELECT * FROM servicos'
        self.cursor.execute(comando)
        servicos = []
        for p in self.cursor.fetchall():
            servicos.append(Servico(p[0], p[1], p[2], p[3]))
        return servicos
    #################################### CRUD VENDAS #####################################################
    def inserirVenda(self,venda):
        self.cursor.execute(
            'INSERT INTO venda(data) VALUES(?)',
            (venda.data))
        self.conexao.commit()

        v = self.cursor.execute('SELECT MAX(codigo) FROM venda')

        for p in venda.pecas:
            self.cursor.execute(
                'INSERT INTO venda_peca(venda_codigo, peca_codigo, quantidade, preco_custo, preco_venda) VALUES(?,?,?,?,?)',
                (v[0][0], p.codigo, p.quantidade, p.preco_compra, p.preco_venda))

        self.conexao.commit()

    def buscarVenda(self,codigo):
        comando = 'SELECT * FROM venda WHERE codigo = ?'
        ven = self.cursor.execute(comando, (codigo,)).fetchall()

        if len(ven)< 1:
            return None

        comando = 'SELECT * FROM venda_peca WHERE venda_codigo = ?'
        venda_peca = self.cursor.execute(comando, (codigo,)).fetchall()

        pecas = []
        for p in venda_peca:
            pecaQuant = PecaQuantidade(self.buscarPeca(p[1]),p[2])
            pecaQuant.preco_custo = p[3]
            pecaQuant.preco_venda =  p[4]
            pecas.append(pecaQuant)

        venda = Venda(codigo,pecas)
        venda.data = ven[0][1]
        return venda

    def deletarVenda(self,codigo):
        venda = self.buscarVenda(codigo)

        comando = 'DELETE FROM pedido_peca WHERE pedido_codigo = ? AND peca_codigo'

        for p in venda.pecas:
            self.cursor.execute(comando, (codigo, p.peca.codigo,))

        comando = 'DELETE FROM venda WHERE codigo = ?'
        self.cursor.execute(comando, (codigo,))

        self.conexao.commit()

    def atualizarVenda(self,venda):
        self.deletarVenda(venda)
        self.inserirVenda(venda)

    def todasVendas(self):
        comando = 'SELECT * FROM venda_peca'
        self.cursor.execute(comando)
        vendas = []
        for v in self.cursor.fetchall():
            vendas.append(self.buscarVenda(v[0]))
        return vendas