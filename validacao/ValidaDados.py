class ValidaDados:
    n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    @staticmethod
    def __isCpf__(cpf):
        if (len(cpf) < 11):
            return False
        for i in list(cpf):
            if (i not in ValidaDados.n):
                return False
        return True

    @staticmethod
    def __isNumeric__(string):

        for i in list(string):
            if i not in ValidaDados.n:
                return False

        return True

