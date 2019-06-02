class EmailInvalidoException(BaseException):
    def __init__(self,email):
        super().__init__()
        self.email = email
    def __str__(self):
        return "O EMAIL \""+self.email +"\" É INVALIDO!!!"