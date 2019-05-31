class EmailInvalidoException(Exception):
    def __init__(self,email):
        self.email = email
    def __str__(self):
        return "O EMAIL "+self.email +" É INVALIDO!!!"