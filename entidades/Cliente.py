from entidades.Pessoa import Pessoa
class Cliente(Pessoa):
    def __init__(self, cpf, nome, endereco, telefone):
        Pessoa.__init__(cpf,nome,endereco,telefone)