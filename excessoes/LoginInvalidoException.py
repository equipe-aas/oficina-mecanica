class LoginInvalidoException(Exception):
    def __init__(self,login):
        self.login = login
    def __str__(self):
        return "O LOGIN "+self.login+" NAO FOI ENCONTRADO!!!"