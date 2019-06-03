import sqlite3
from entidades.Cliente import Cliente

class ConexaoDataBase:
    def __init__(self):
        self.conexao = sqlite3.connect('database.sqlite')
        self.cursor = self.conexao.cursor()

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