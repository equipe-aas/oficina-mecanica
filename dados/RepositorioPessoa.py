class RepositorioPessoa:
    def __init__(self):
        self.pessoas = []
    def adicionar(self,pessoa):
        self.pessoas.append(pessoa)
    def remover(self,pessoa):
        self.pessoas.remove(pessoa)
    def buscar(self,cpf):
        pessoa = None
        for p in self.pessoas:
            if p.cpf == cpf:
                pessoa = p
                break
        return pessoa
    def __str__(self):
        string = ""
        for p in self.pessoas:
            string += p.str + "\n"
        return string