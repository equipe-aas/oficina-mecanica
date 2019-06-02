class LoginInvalidoException(BaseException):
    def __init__(self,login):
        super().__init__()
        self.login = login
    def __str__(self):
        return "O LOGIN \""+self.login+"\" NAO FOI ENCONTRADO!!!"